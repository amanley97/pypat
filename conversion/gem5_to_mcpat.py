import argparse
import json
import os
import re
import h5py
import io
import xml.etree.ElementTree as ET
from .templates import O3CPU_TEMPLATE


def parse_template(source):
    return ET.parse(source, parser=ET.XMLParser(target=ET.TreeBuilder(insert_comments=True)))

def load_template():
    return ET.parse(io.StringIO(O3CPU_TEMPLATE))

def read_config_file(config_file):
    print(f"Reading config from: {config_file}")
    with open(config_file, "r") as f:
        return json.load(f)

def read_mcpat_file(template_file):
    print(f"Reading McPAT template from: {template_file}")
    return parse_template(template_file)


def get_conf_value(conf_str, config):
    parts = conf_str.split('.')
    curr = config
    for i, key in enumerate(parts):
        if isinstance(curr, list):
            if curr and isinstance(curr[0], dict) and key in curr[0]:
                curr = curr[0][key]
            else:
                return 0
        elif isinstance(curr, dict):
            if key not in curr:
                return 0
            curr = curr[key]
        else:
            return 0

        if '.'.join(parts[:i + 1]) == "system.cpu_clk_domain.clock":
            if isinstance(curr, list) and curr and isinstance(curr[0], (int, float)):
                curr = curr[0] / 1e12
            else:
                curr = 0
    return curr


def read_stats_file(stats_file):
    print(f"Reading GEM5 stats from HDF5: {stats_file}")
    stats = {}

    def extract(group, prefix=""):
        result = {}
        for key, item in group.items():
            path = f"{prefix}.{key}" if prefix else key
            if isinstance(item, h5py.Group):
                result.update(extract(item, path))
            elif isinstance(item, h5py.Dataset):
                try:
                    val = item[()]
                    if hasattr(val, "shape") and val.shape != ():  # Array
                        scalar = float(val.flatten()[-1])  # last value
                    else:
                        scalar = float(val)
                    result[path] = str(scalar)
                except Exception:
                    result[path] = "0.0"
        return result

    stats[0] = extract(h5py.File(stats_file, 'r'))
    return stats


def dump_mcpat_out(stats, config, template_mcpat, outfile, itr=0):
    config_match = re.compile(r'config\.([a-zA-Z0-9_:\.]+)')
    stat_match = re.compile(r'stats\.([a-zA-Z0-9_:\.]+)')

    def eval_expr(expr):
        expr = expr.strip("()")
        return ','.join(str(eval(x.strip())) for x in expr.split(','))

    root = template_mcpat.getroot()

    for param in root.iter('param'):
        value = param.attrib['value']
        if 'config' in value:
            for match in config_match.findall(value):
                value = value.replace(f"config.{match}", str(get_conf_value(match, config)))
            value = eval_expr(value) if "," in value else str(eval(value.replace('[', '').replace(']', '')))
            param.attrib['value'] = value

    for stat in root.iter('stat'):
        value = stat.attrib['value']
        if 'stats' in value:
            expr = value
            for match in stat_match.findall(value):
                expr = expr.replace(f"stats.{match}", stats[0].get(match, "0.0"))
            stat.attrib['value'] = str(eval(expr) if "/ 0.0" not in expr else 0)

    print(f"Writing input to McPAT in: {outfile}")
    template_mcpat.write(outfile)

    for pattern in [
        ('<stat name="clock_rate_dvfs"', '<param name="clock_rate_dvfs"'),
        ('<stat name="vdd_dvfs"', '<param name="vdd_dvfs"'),
        ('stat name="sim_second', 'param name="sim_second'),
        ('stat name="sim_ticks', 'param name="sim_ticks')
    ]:
        os.system(f"sed -i 's/{pattern[0]}/{pattern[1]}/g' {outfile}")

def run_conversion(stats_file, config_file, outfile, template=None):
    stats = read_stats_file(stats_file)
    config = read_config_file(config_file)
    if template is not None:
        template_file = read_mcpat_file(template)
    else:
        template_file = load_template()
    dump_mcpat_out(stats, config, template_file, outfile)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert gem5 stats/config to McPAT XML input")
    parser.add_argument("stats_file", help="Path to gem5 stats (.h5) file")
    parser.add_argument("config_file", help="Path to gem5 config (.json) file")
    parser.add_argument("-t", "--template", default=None, help="Path to McPAT template (.xml)")
    parser.add_argument("-o", "--outfile", default=".", help="Output directory")
    parser.add_argument("-q", "--quiet", dest="verbose", action="store_false", help="Suppress verbose output")
    args = parser.parse_args()
    
    run_conversion(
        stats_file=args.stats_file,
        config_file=args.config_file,
        outfile=args.outfile,
        template=args.template
    )