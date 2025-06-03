O3CPU_TEMPLATE = """<?xml version='1.0' encoding='utf-8'?>
<component id="root" name="root">
  <component id="system" name="system">
    <param name="number_of_cores" value="1" />
    <param name="number_of_L1Directories" value="0" />
    <param name="number_of_L2Directories" value="0" />
    <param name="number_of_L2s" value="1" />
    <param name="Private_L2" value="0" />
    <param name="number_of_L3s" value="0" />
    <param name="number_of_NoCs" value="1" />
    <param name="homogeneous_cores" value="1" />
    <param name="homogeneous_L2s" value="1" />
    <param name="homogeneous_L1Directories" value="0" />
    <param name="homogeneous_L2Directories" value="0" />
    <param name="homogeneous_L3s" value="0" />
    <param name="homogeneous_ccs" value="1" />
    <param name="homogeneous_NoCs" value="0" />
    <param name="core_tech_node" value="40" />
    <param name="temperature" value="340" />
    <param name="number_cache_levels" value="2" />
    <param name="interconnect_projection_type" value="1" />
    <param name="device_type" value="2" />
    <param name="longer_channel_device" value="1" />
    <param name="Embedded" value="1" />
    <param name="opt_clockrate" value="1" />
    <param name="machine_bits" value="64" />
    <param name="virtual_address_width" value="64" />
    <param name="physical_address_width" value="52" />
    <param name="virtual_memory_page_size" value="4096" />
    <param name="target_core_clockrate" value="1e6/config.system.clk_domain.clock" />
    <stat name="total_cycles" value="stats.system.cpu.numCycles + stats.system.cpu1.numCycles" />
    <stat name="idle_cycles" value="stats.system.cpu.idleCycles + stats.system.cpu1.idleCycles" />
    <stat name="busy_cycles" value="stats.system.cpu.numCycles - stats.system.cpu.idleCycles + stats.system.cpu1.numCycles - stats.system.cpu1.idleCycles" />
    <component id="system.core0" name="core0">
      <param name="clock_rate" value="1e6/config.system.clk_domain.clock" />
      <param name="vdd" value="1.25" />
      <param name="power_gating_vcc" value="-1" />
      <param name="opt_local" value="0" />
      <param name="instruction_length" value="32" />
      <param name="opcode_width" value="16" />
      <param name="x86" value="0" />
      <param name="micro_opcode_width" value="8" />
      <param name="machine_type" value="0" />
      <param name="number_hardware_threads" value="config.system.cpu.numThreads" />
      <param name="fetch_width" value="config.system.cpu.fetchWidth" />
      <param name="number_instruction_fetch_ports" value="1" />
      <param name="decode_width" value="config.system.cpu.decodeWidth" />
      <param name="issue_width" value="config.system.cpu.issueWidth" />
      <param name="peak_issue_width" value="config.system.cpu.issueWidth" />
      <param name="commit_width" value="config.system.cpu.commitWidth" />
      <param name="fp_issue_width" value="2" />
      <param name="prediction_width" value="1" />
      <param name="pipelines_per_core" value="1,1" />
      <param name="pipeline_depth" value="31,31" />
      <param name="ALU_per_core" value="6" />
      <param name="MUL_per_core" value="1" />
      <param name="FPU_per_core" value="2" />
      <param name="instruction_buffer_size" value="32" />
      <param name="decoded_stream_buffer_size" value="16" />
      <param name="instruction_window_scheme" value="0" />
      <param name="instruction_window_size" value="config.system.cpu.numIQEntries" />
      <param name="fp_instruction_window_size" value="config.system.cpu.numIQEntries" />
      <param name="ROB_size" value="config.system.cpu.numROBEntries" />
      <param name="archi_Regs_IRF_size" value="16" />
      <param name="archi_Regs_FRF_size" value="32" />
      <param name="phy_Regs_IRF_size" value="config.system.cpu.numPhysIntRegs" />
      <param name="phy_Regs_FRF_size" value="config.system.cpu.numPhysFloatRegs" />
      <param name="rename_scheme" value="0" />
      <param name="register_windows_size" value="0" />
      <param name="LSU_order" value="inorder" />
      <param name="store_buffer_size" value="config.system.cpu.SQEntries" />
      <param name="load_buffer_size" value="config.system.cpu.LQEntries" />
      <param name="memory_ports" value="2" />
      <param name="RAS_size" value="config.system.cpu.branchPred.ras.numEntries + config.system.cpu.branchPred.RASSize" />
      <stat name="total_instructions" value="stats.system.cpu.statIssuedInstType_0::total + stats.system.cpu1.statIssuedInstType_0::total" />
      <stat name="int_instructions" value="stats.system.cpu.statIssuedInstType_0::No_OpClass + stats.system.cpu1.statIssuedInstType_0::No_OpClass + stats.system.cpu.statIssuedInstType_0::IntAlu + stats.system.cpu1.statIssuedInstType_0::IntAlu + stats.system.cpu.statIssuedInstType_0::IntMult + stats.system.cpu1.statIssuedInstType_0::IntMult + stats.system.cpu.statIssuedInstType_0::IntDiv + stats.system.cpu1.statIssuedInstType_0::IntDiv + stats.system.cpu.statIssuedInstType_0::IprAccess + stats.system.cpu1.statIssuedInstType_0::IprAccess" />
      <stat name="fp_instructions" value="stats.system.cpu.statFuBusy::FloatAdd + stats.system.cpu1.statFuBusy::FloatAdd + stats.system.cpu.statFuBusy::FloatCmp + stats.system.cpu1.statFuBusy::FloatCmp + stats.system.cpu.statFuBusy::FloatCvt + stats.system.cpu1.statFuBusy::FloatCvt + stats.system.cpu.statFuBusy::FloatMult + stats.system.cpu1.statFuBusy::FloatMult + stats.system.cpu.statFuBusy::FloatDiv + stats.system.cpu1.statFuBusy::FloatDiv + stats.system.cpu.statFuBusy::FloatSqrt + stats.system.cpu1.statFuBusy::FloatSqrt" />
      <stat name="branch_instructions" value="stats.system.cpu.branchPred.condPredicted + stats.system.cpu1.branchPred.condPredicted" />
      <stat name="branch_mispredictions" value="stats.system.cpu.branchPred.condIncorrect + stats.system.cpu1.branchPred.condIncorrect" />
      <stat name="load_instructions" value="stats.system.cpu.commit.committedInstType_0::MemRead + stats.system.cpu1.commit.committedInstType_0::MemRead + stats.system.cpu.commit.committedInstType_0::InstPrefetch + stats.system.cpu1.commit.committedInstType_0::InstPrefetch" />
      <stat name="store_instructions" value="stats.system.cpu.commit.committedInstType_0::MemWrite + stats.system.cpu1.commit.committedInstType_0::MemWrite" />
      <stat name="committed_instructions" value="stats.system.cpu.commit.instsCommitted + stats.system.cpu1.commit.instsCommitted" />
      <stat name="committed_int_instructions" value="stats.system.cpu.commit.integer + stats.system.cpu1.commit.integer" />
      <stat name="committed_fp_instructions" value="stats.system.cpu.commit.floating + stats.system.cpu1.commit.floating" />
      <stat name="pipeline_duty_cycle" value="1" />
      <stat name="total_cycles" value="stats.system.cpu.numCycles + stats.system.cpu1.numCycles" />
      <stat name="idle_cycles" value="stats.system.cpu.idleCycles + stats.system.cpu1.idleCycles" />
      <stat name="busy_cycles" value="stats.system.cpu.numCycles + stats.system.cpu1.numCycles - stats.system.cpu.idleCycles + stats.system.cpu1.idleCycles" />
      <stat name="ROB_reads" value="stats.system.cpu.rob.reads + stats.system.cpu1.rob.reads" />
      <stat name="ROB_writes" value="stats.system.cpu.rob.writes + stats.system.cpu1.rob.writes" />
      <stat name="rename_reads" value="stats.system.cpu.rename.intLookups + stats.system.cpu1.rename.intLookups" />
      <stat name="rename_writes" value="int(stats.system.cpu.rename.renamedOperands * stats.system.cpu.rename.intLookups / stats.system.cpu.rename.lookups) + int(stats.system.cpu1.rename.renamedOperands * stats.system.cpu1.rename.intLookups / stats.system.cpu1.rename.lookups)" />
      <stat name="fp_rename_reads" value="stats.system.cpu.rename.fpLookups + stats.system.cpu1.rename.fpLookups" />
      <stat name="fp_rename_writes" value="int(stats.system.cpu.rename.renamedOperands * stats.system.cpu.rename.fpLookups / stats.system.cpu.rename.lookups) + int(stats.system.cpu1.rename.renamedOperands * stats.system.cpu1.rename.fpLookups / stats.system.cpu1.rename.lookups)" />
      <stat name="inst_window_reads" value="stats.system.cpu.intInstQueueReads + stats.system.cpu1.intInstQueueReads" />
      <stat name="inst_window_writes" value="stats.system.cpu.intInstQueueWrites + stats.system.cpu1.intInstQueueWrites" />
      <stat name="inst_window_wakeup_accesses" value="stats.system.cpu.intInstQueueWakeupAccesses + stats.system.cpu1.intInstQueueWakeupAccesses" />
      <stat name="fp_inst_window_reads" value="stats.system.cpu.fpInstQueueReads + stats.system.cpu1.fpInstQueueReads" />
      <stat name="fp_inst_window_writes" value="stats.system.cpu.fpInstQueueWrites + stats.system.cpu1.fpInstQueueWrites" />
      <stat name="fp_inst_window_wakeup_accesses" value="stats.system.cpu.fpInstQueueWakeupAccesses + stats.system.cpu1.fpInstQueueWakeupAccesses" />
      <stat name="int_regfile_reads" value="stats.system.cpu.intRegfileReads + stats.system.cpu1.intRegfileReads" />
      <stat name="float_regfile_reads" value="stats.system.cpu.fpRegfileReads + stats.system.cpu1.fpRegfileReads" />
      <stat name="int_regfile_writes" value="stats.system.cpu.intRegfileWrites + stats.system.cpu1.intRegfileWrites" />
      <stat name="float_regfile_writes" value="stats.system.cpu.fpRegfileWrites + stats.system.cpu1.fpRegfileWrites" />
      <stat name="function_calls" value="stats.system.cpu.commit.functionCalls + stats.system.cpu1.commit.functionCalls" />
      <stat name="ialu_accesses" value="stats.system.cpu.intAluAccesses + stats.system.cpu1.intAluAccesses" />
      <stat name="fpu_accesses" value="stats.system.cpu.fpAluAccesses + stats.system.cpu1.fpAluAccesses" />
      <stat name="mul_accesses" value="0" />
      <stat name="cdb_alu_accesses" value="0" />
      <stat name="cdb_mul_accesses" value="0" />
      <stat name="cdb_fpu_accesses" value="0" />
      <stat name="IFU_duty_cycle" value="0.25" />
      <stat name="LSU_duty_cycle" value="0.25" />
      <stat name="MemManU_I_duty_cycle" value="0.25" />
      <stat name="MemManU_D_duty_cycle" value="0.25" />
      <stat name="ALU_duty_cycle" value="1" />
      <stat name="MUL_duty_cycle" value="0.3" />
      <stat name="FPU_duty_cycle" value="0.3" />
      <stat name="ALU_cdb_duty_cycle" value="1" />
      <stat name="MUL_cdb_duty_cycle" value="0.3" />
      <stat name="FPU_cdb_duty_cycle" value="0.3" />
      <param name="number_of_BPT" value="2" />
      <param name="number_of_BTB" value="2" />
      <component id="system.core0.predictor" name="PBT">
        <param name="local_predictor_size" value="10,3" />
        <param name="local_predictor_entries" value="1024" />
        <param name="global_predictor_entries" value="4096" />
        <param name="global_predictor_bits" value="2" />
        <param name="chooser_predictor_entries" value="4096" />
        <param name="chooser_predictor_bits" value="2" />
      </component>
      <component id="system.core0.itlb" name="itlb">
        <param name="number_entries" value="config.system.cpu.mmu.itb.size" />
        <stat name="total_accesses" value="stats.system.cpu.mmu.itb.rdAccesses + stats.system.cpu1.mmu.itb.rdAccesses + stats.system.cpu.mmu.itb.wrAccesses + stats.system.cpu1.mmu.itb.wrAccesses" />
        <stat name="total_misses" value="stats.system.cpu.mmu.itb.rdMisses + stats.system.cpu1.mmu.itb.rdMisses + stats.system.cpu.mmu.itb.wrMisses + stats.system.cpu1.mmu.itb.wrMisses" />
        <stat name="conflicts" value="0" />
      </component>
      <component id="system.core0.icache" name="icache">
        <param name="icache_config" value="config.system.cpu.icache.size,config.system.cpu.icache.tags.block_size,config.system.cpu.icache.assoc,1,1,config.system.cpu.icache.response_latency,config.system.cpu.icache.tags.block_size,0" />
        <param name="buffer_sizes" value="config.system.cpu.icache.mshrs,config.system.cpu.icache.mshrs,config.system.cpu.icache.mshrs,config.system.cpu.icache.mshrs" />
        <stat name="read_accesses" value="stats.system.cpu.icache.ReadReq.accesses::total + stats.system.cpu1.icache.ReadReq.accesses::total" />
        <stat name="read_misses" value="stats.system.cpu.icache.ReadReq.misses::total + stats.system.cpu1.icache.ReadReq.misses::total" />
        <stat name="conflicts" value="stats.system.cpu.icache.replacements + stats.system.cpu1.icache.replacements" />
      </component>
      <component id="system.core0.dtlb" name="dtlb">
        <param name="number_entries" value="config.system.cpu.mmu.dtb.size" />
        <stat name="total_accesses" value="stats.system.cpu.mmu.dtb.accesses + stats.system.cpu1.mmu.dtb.accesses" />
        <stat name="total_misses" value="stats.system.cpu.mmu.dtb.misses + stats.system.cpu1.mmu.dtb.misses" />
        <stat name="conflicts" value="0" />
      </component>
      <component id="system.core0.dcache" name="dcache">
        <param name="dcache_config" value="config.system.cpu.dcache.size,config.system.cpu.dcache.tags.block_size,config.system.cpu.dcache.assoc,1,1,config.system.cpu.dcache.response_latency,config.system.cpu.dcache.tags.block_size,0" />
        <param name="buffer_sizes" value="config.system.cpu.dcache.mshrs,config.system.cpu.dcache.mshrs,config.system.cpu.dcache.mshrs,config.system.cpu.dcache.mshrs" />
        <stat name="read_accesses" value="stats.system.cpu.dcache.ReadReq.accesses::total + stats.system.cpu1.dcache.ReadReq.accesses::total" />
        <stat name="write_accesses" value="stats.system.cpu.dcache.WriteReq.accesses::total + stats.system.cpu1.dcache.WriteReq.accesses::total" />
        <stat name="read_misses" value="stats.system.cpu.dcache.ReadReq.misses::total + stats.system.cpu1.dcache.ReadReq.misses::total" />
        <stat name="write_misses" value="stats.system.cpu.dcache.WriteReq.misses::total + stats.system.cpu1.dcache.WriteReq.misses::total" />
        <stat name="conflicts" value="stats.system.cpu.dcache.replacements + stats.system.cpu1.dcache.replacements" />
      </component>
      <component id="system.core0.BTB" name="BTB">
        <param name="BTB_config" value="4096,4,2, 2, 1,1" />
        <stat name="read_accesses" value="stats.system.cpu.branchPred.BTBLookups + stats.system.cpu1.branchPred.BTBLookups" />
        <stat name="write_accesses" value="stats.system.cpu.commit.branches + stats.system.cpu1.commit.branches" />
      </component>
    </component>
    <component id="system.L20" name="L20">
      <param name="L2_config" value="config.system.l2cache.size,config.system.l2cache.tags.block_size,config.system.l2cache.assoc,1,1,config.system.l2cache.data_latency,config.system.l2cache.tags.block_size,1" />
      <param name="buffer_sizes" value="config.system.l2cache.mshrs,config.system.l2cache.mshrs,config.system.l2cache.mshrs,config.system.l2cache.mshrs" />
      <param name="clockrate" value="3400" />
      <param name="ports" value="1,1,1" />
      <param name="device_type" value="0" />
      <stat name="read_accesses" value="stats.system.l2cache.ReadSharedReq.accesses::total + stats.system.cpu1.l2cache.ReadSharedReq.accesses::total" />
      <stat name="write_accesses" value="stats.system.l2cache.ReadExReq.accesses::total + stats.system.cpu1.l2cache.ReadExReq.accesses::total" />
      <stat name="read_misses" value="stats.system.l2cache.ReadSharedReq.misses::total + stats.system.cpu1.l2cache.ReadSharedReq.misses::total" />
      <stat name="write_misses" value="stats.system.l2cache.ReadExReq.misses::total + stats.system.cpu1.l2cache.ReadExReq.misses::total" />
      <stat name="conflicts" value="0" />
      <stat name="duty_cycle" value="1.0" />
    </component>
    <component id="system.NoC0" name="noc0">
      <param name="clockrate" value="3400" />
      <param name="vdd" value="0" />
      <param name="power_gating_vcc" value="-1" />
      <param name="type" value="0" />
      <param name="horizontal_nodes" value="1" />
      <param name="vertical_nodes" value="1" />
      <param name="has_global_link" value="0" />
      <param name="link_throughput" value="1" />
      <param name="link_latency" value="1" />
      <param name="input_ports" value="1" />
      <param name="output_ports" value="1" />
      <param name="flit_bits" value="256" />
      <param name="chip_coverage" value="1" />
      <param name="link_routing_over_percentage" value="0.5" />
      <stat name="total_accesses" value="100000" />
      <stat name="duty_cycle" value="1" />
    </component>
    <component id="system.mc" name="mc">
      <param name="type" value="0" />
      <param name="mc_clock" value="config.system.clk_domain.clock.0" />
      <param name="vdd" value="0" />
      <param name="power_gating_vcc" value="-1" />
      <param name="peak_transfer_rate" value="1200" />
      <param name="block_size" value="64" />
      <param name="number_mcs" value="1" />
      <param name="memory_channels_per_mc" value="config.system.mem_ctrls.0.channels" />
      <param name="number_ranks" value="2" />
      <param name="withPHY" value="config.system.mem_ctrls.0.ranks_per_channel" />
      <param name="req_window_size_per_channel" value="32" />
      <param name="IO_buffer_size_per_channel" value="32" />
      <param name="databus_width" value="128" />
      <param name="addressbus_width" value="51" />
      <stat name="memory_accesses" value="(stats.system.mem_ctrls.readReqs + stats.system.mem_ctrls.writeReqs)" />
      <stat name="memory_reads" value="stats.system.mem_ctrls.readReqs" />
      <stat name="memory_writes" value="stats.system.mem_ctrls.writeReqs" />
    </component>
    <component id="system.niu" name="niu">
      <param name="type" value="0" />
      <param name="clockrate" value="350" />
      <param name="vdd" value="0" />
      <param name="power_gating_vcc" value="-1" />
      <param name="number_units" value="0" />
      <stat name="duty_cycle" value="1.0" />
      <stat name="total_load_perc" value="0.7" />
    </component>
    <component id="system.pcie" name="pcie">
      <param name="type" value="0" />
      <param name="withPHY" value="1" />
      <param name="clockrate" value="350" />
      <param name="vdd" value="0" />
      <param name="power_gating_vcc" value="-1" />
      <param name="number_units" value="0" />
      <param name="num_channels" value="8" />
      <stat name="duty_cycle" value="1.0" />
      <stat name="total_load_perc" value="0.7" />
    </component>
    <component id="system.flashc" name="flashc">
      <param name="number_flashcs" value="0" />
      <param name="type" value="1" />
      <param name="withPHY" value="1" />
      <param name="peak_transfer_rate" value="200" />
      <param name="vdd" value="0" />
      <param name="power_gating_vcc" value="-1" />
      <stat name="duty_cycle" value="1.0" />
      <stat name="total_load_perc" value="0.7" />
    </component>
  </component>
</component>
"""