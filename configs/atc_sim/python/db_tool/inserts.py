# coding=utf-8

from datetime import date

from probe_basic_db_tool.tool_table import ToolTable, Tool, ProbeParams, CutParams
from probe_basic_db_tool.base import Session, engine, Base


Base.metadata.create_all(engine)

session = Session()

################################################
#
# Probe Parameters
#
################################################


probe_params_1 = ProbeParams(
    tool_diameter_probe_mode = "0.0",
    tool_diameter_offset_mode = "0.0",
    tool_diameter = "0.0",
    tool_breakage_detection_mode = "0.0",
    tool_breakage_tolerance = "0.0"
)

probe_params_2 = ProbeParams(
    tool_diameter_probe_mode = "0.0",
    tool_diameter_offset_mode = "0.0",
    tool_diameter = "0.0",
    tool_breakage_detection_mode = "0.0",
    tool_breakage_tolerance = "0.0"
)

probe_params_3 = ProbeParams(
    tool_diameter_probe_mode = "0.0",
    tool_diameter_offset_mode = "0.0",
    tool_diameter = "0.0",
    tool_breakage_detection_mode = "0.0",
    tool_breakage_tolerance = "0.0"
)

################################################
#
# ISO 13399 Cut Parameters 
# https://www.sandvik.coromant.com/en-us/knowledge/machining-formulas-definitions/cutting-tool-parameters
################################################
cut_params_1 = CutParams(
    ALP = 0.0,   # Clearance angle axial
    ANN = 0.0,   # Clearance angle minor
    APMX = 0.0,  # Depth of cut maximum
    B = 0.0,   # Shank width
    BAWS = 0.0,   # Body angle workpiece side
    BBD = 0.0,   # Balanced by design
    BBR = 0.0,  # Balanced by rotational test
    BD = 0.0,  # Body diameter
    BHTA = 0.0,   # Body half taper angle
    BS = 0.0,   # Wiper edge length
    BSG = 0.0,   # Basic standard group
    CDX = 0.0,   # Cutting depth maximum
    CHW = 0.0,   # Corner chamfer width
    CICT = 0.0,   # Cutting item count
    CND = 0.0,   # Coolant entry diameter
    CNSC = 0.0,   # Coolant entry style code
    COATING = 0.0,   # Coating
    CNT = 0.0,   # Coolant entry thread size
    CP = 0.0,   # Coolant pressure
    CRKS = 0.0,   # Connection retention knob thread size
    CTPT = 0.0,   # Operation type
    CUTDIA = 0.0,   # Work piece parting diameter maximum
    CW = 0.0,   # Cutting width
    CWTOLL = 0.0,   # Cutting width lower tolerance
    CWTOLU = 0.0,   # Cutting width upper tolerance
    CXSC = 0.0,   # Coolant exit style code
    CZC = 0.0,   # Connection size code
    CZC_MS = 0.0,   # Connection size code machine side
    CZC_WS = 0.0,   # Connection size code workpiece side
    DAH = 0.0,   # Diameter access hole
    DAXIN = 0.0,   # Axial groove inside diameter minimum
    DAXX = 0.0,   # Axial groove outside diameter maximum
    DBC = 0.0,   # Diameter bolt circle
    DC = 0.0,   # Cutting diameter
    DCB = 0.0,   # Connection bore diameter
    DCBN = 0.0,   # Connection bore diameter minimum
    DCBX = 0.0,   # Connection bore diameter maximum
    DCF = 0.0,   # Cutting diameter face contact
    DCON = 0.0,   # Connection diameter
    DCSFMS = 0.0,   # Contact surface diameter machine side
    DCSFWS = 0.0,   # Contact surface diameter workpiece side
    DCX = 0.0,   # Maximum cutting diameter
    DIX = 0.0,   # Tool changer interference diameter maximum
    DMIN = 0.0,   # Minimum bore diameter
    DMM = 0.0,   # Shank diameter
    DN = 0.0,   # Neck diameter
    DSGN = 0.0,   # Design
    D1 = 0.0,   # Fixing hole diameter
    FHA = 0.0,   # Flute helix angle
    FLGT = 0.0,   # Flange thickness
    FTDZ = 0.0,   # For thread diameter size
    H = 0.0,  # Shank height
    HF = 0.0,   # Functional height
    HRY = 0.0,   # Lowest point from reference plain
    HTB = 0.0,   # Body height
    HTH = 0.0,   # Height
    IC = 0.0,   # Inscribed circle diameter
    INSL = 0.0,   # Insert length
    IZC = 0.0,   # Insert size code
    KAPR = 0.0,   # Tool cutting edge angle
    KCH = 0.0,   # Corner chamfer
    L = 0.0,   # Cutting edge length
    LB = 0.0,   # Body length
    LCF = 0.0,   # Length chip flute
    LE = 0.0,   # Cutting edge effective length
    LF = 0.0,   # Functional length
    LGR = 0.0,   # Regrind length
    LH = 0.0,   # Head length
    LPR = 0.0,   # Protruding length
    LS = 0.0,   # Shank length
    LSC = 0.0,   # Clamping length
    LSCN = 0.0,   # Clamping length minimum
    LSCX = 0.0,   # Clamping length maximum
    LSD = 0.0,   # Dead shank length
    LU = 0.0,   # Usable length (max. recommended)
    MHD = 0.0,   # Mounting hole distance
    MIID = 0.0,   # Master insert identification
    MMCC = 0.0,   # Code for preset torque
    NOF = 0.0,   # Flute count
    OAH = 0.0,   # Overall height
    OAL = 0.0,   # Overall length
    OAW = 0.0,   # Overall width
    OHN = 0.0,   # Overhang minimum
    OHX = 0.0,   # Overhang maximum
    PHD = 0.0,   # Premachined hole diameter
    PHDX = 0.0,  # Premachined hole diameter maximum
    PL = 0.0,   # Point length
    PRFRAD = 0.0,   # Profile radius
    PRSPC = 0.0,   # Profile specification
    PSIR = 0.0,   # Tool lead angle
    PSIRL = 0.0,   # Cutting edge angle major left hand
    PSIRR  = 0.0,  # Cutting edge angle major right hand
    RADH = 0.0,   # Radial body height
    RADW = 0.0,   # Radial body width
    RE = 0.0,   # Corner radius
    RETOLL = 0.0,   # Corner radius lower tolerance
    RETOLU = 0.0,   # Corner radius upper tolerance
    RPMX = 0.0,   # Rotational speed maximum
    S = 0.0,   # Insert thickness
    SDL = 0.0,   # Step diameter length
    SIG = 0.0,   # Point angle
    SSC = 0.0,   # Insert seat size code
    SUBSTRATE = 0.0,   # Substrate
    TCDC = 0.0,  # Tolerance class cutting diameter
    TCDMM = 0.0,   # Shank diameter tolerance
    TCHA = 0.0,   # Achievable hole tolerance
    TCT = 0.0,   # Tolerance class tool
    TCTR = 0.0,   # Thread tolerance class
    TD = 0.0,   # Thread diameter
    TDZ = 0.0,   # Thread diameter size
    TFLA = 0.0,   # Tap floating length ahead
    TFLB = 0.0,   # Tap floating length behind
    THCHT = 0.0,   # Threading chamfer type
    THFT = 0.0,   # Form type
    THLGTH = 0.0,   # Thread length
    THUB = 0.0,   # Hub thickness
    TP = 0.0,   # Thread pitch
    TPI = 0.0,   # Threads per inch
    TPIN = 0.0,   # Threads per inch minimum
    TPIX = 0.0,   # Threads per inch maximum
    TPN = 0.0,   # Thread pitch minimum
    TPX = 0.0,   # Thread pitch maximum
    TQ = 0.0,   # Torque
    TSYC = 0.0,   # Tool style code
    ULDR = 0.0,   # Usable length diameter ratio
    WB = 0.0,   # Body width
    WF = 0.0,   # Functional width
    WSC = 0.0,   # Clamping width
    WT = 0.0,   # Weight of item
    W1 = 0.0,   # Insert width
    ZEFF = 0.0,   # Face effective cutting edge count
    ZEFP = 0.0,   # Peripheral effective cutting edge count
    ZWX = 0.0   # Number of Wiper inserts maximum
)

cut_params_2 = CutParams(
    ALP = 0.0,   # Clearance angle axial
    ANN = 0.0,   # Clearance angle minor
    APMX = 0.0,  # Depth of cut maximum
    B = 0.0,   # Shank width
    BAWS = 0.0,   # Body angle workpiece side
    BBD = 0.0,   # Balanced by design
    BBR = 0.0,  # Balanced by rotational test
    BD = 0.0,  # Body diameter
    BHTA = 0.0,   # Body half taper angle
    BS = 0.0,   # Wiper edge length
    BSG = 0.0,   # Basic standard group
    CDX = 0.0,   # Cutting depth maximum
    CHW = 0.0,   # Corner chamfer width
    CICT = 0.0,   # Cutting item count
    CND = 0.0,   # Coolant entry diameter
    CNSC = 0.0,   # Coolant entry style code
    COATING = 0.0,   # Coating
    CNT = 0.0,   # Coolant entry thread size
    CP = 0.0,   # Coolant pressure
    CRKS = 0.0,   # Connection retention knob thread size
    CTPT = 0.0,   # Operation type
    CUTDIA = 0.0,   # Work piece parting diameter maximum
    CW = 0.0,   # Cutting width
    CWTOLL = 0.0,   # Cutting width lower tolerance
    CWTOLU = 0.0,   # Cutting width upper tolerance
    CXSC = 0.0,   # Coolant exit style code
    CZC = 0.0,   # Connection size code
    CZC_MS = 0.0,   # Connection size code machine side
    CZC_WS = 0.0,   # Connection size code workpiece side
    DAH = 0.0,   # Diameter access hole
    DAXIN = 0.0,   # Axial groove inside diameter minimum
    DAXX = 0.0,   # Axial groove outside diameter maximum
    DBC = 0.0,   # Diameter bolt circle
    DC = 0.0,   # Cutting diameter
    DCB = 0.0,   # Connection bore diameter
    DCBN = 0.0,   # Connection bore diameter minimum
    DCBX = 0.0,   # Connection bore diameter maximum
    DCF = 0.0,   # Cutting diameter face contact
    DCON = 0.0,   # Connection diameter
    DCSFMS = 0.0,   # Contact surface diameter machine side
    DCSFWS = 0.0,   # Contact surface diameter workpiece side
    DCX = 0.0,   # Maximum cutting diameter
    DIX = 0.0,   # Tool changer interference diameter maximum
    DMIN = 0.0,   # Minimum bore diameter
    DMM = 0.0,   # Shank diameter
    DN = 0.0,   # Neck diameter
    DSGN = 0.0,   # Design
    D1 = 0.0,   # Fixing hole diameter
    FHA = 0.0,   # Flute helix angle
    FLGT = 0.0,   # Flange thickness
    FTDZ = 0.0,   # For thread diameter size
    H = 0.0,  # Shank height
    HF = 0.0,   # Functional height
    HRY = 0.0,   # Lowest point from reference plain
    HTB = 0.0,   # Body height
    HTH = 0.0,   # Height
    IC = 0.0,   # Inscribed circle diameter
    INSL = 0.0,   # Insert length
    IZC = 0.0,   # Insert size code
    KAPR = 0.0,   # Tool cutting edge angle
    KCH = 0.0,   # Corner chamfer
    L = 0.0,   # Cutting edge length
    LB = 0.0,   # Body length
    LCF = 0.0,   # Length chip flute
    LE = 0.0,   # Cutting edge effective length
    LF = 0.0,   # Functional length
    LGR = 0.0,   # Regrind length
    LH = 0.0,   # Head length
    LPR = 0.0,   # Protruding length
    LS = 0.0,   # Shank length
    LSC = 0.0,   # Clamping length
    LSCN = 0.0,   # Clamping length minimum
    LSCX = 0.0,   # Clamping length maximum
    LSD = 0.0,   # Dead shank length
    LU = 0.0,   # Usable length (max. recommended)
    MHD = 0.0,   # Mounting hole distance
    MIID = 0.0,   # Master insert identification
    MMCC = 0.0,   # Code for preset torque
    NOF = 0.0,   # Flute count
    OAH = 0.0,   # Overall height
    OAL = 0.0,   # Overall length
    OAW = 0.0,   # Overall width
    OHN = 0.0,   # Overhang minimum
    OHX = 0.0,   # Overhang maximum
    PHD = 0.0,   # Premachined hole diameter
    PHDX = 0.0,  # Premachined hole diameter maximum
    PL = 0.0,   # Point length
    PRFRAD = 0.0,   # Profile radius
    PRSPC = 0.0,   # Profile specification
    PSIR = 0.0,   # Tool lead angle
    PSIRL = 0.0,   # Cutting edge angle major left hand
    PSIRR  = 0.0,  # Cutting edge angle major right hand
    RADH = 0.0,   # Radial body height
    RADW = 0.0,   # Radial body width
    RE = 0.0,   # Corner radius
    RETOLL = 0.0,   # Corner radius lower tolerance
    RETOLU = 0.0,   # Corner radius upper tolerance
    RPMX = 0.0,   # Rotational speed maximum
    S = 0.0,   # Insert thickness
    SDL = 0.0,   # Step diameter length
    SIG = 0.0,   # Point angle
    SSC = 0.0,   # Insert seat size code
    SUBSTRATE = 0.0,   # Substrate
    TCDC = 0.0,  # Tolerance class cutting diameter
    TCDMM = 0.0,   # Shank diameter tolerance
    TCHA = 0.0,   # Achievable hole tolerance
    TCT = 0.0,   # Tolerance class tool
    TCTR = 0.0,   # Thread tolerance class
    TD = 0.0,   # Thread diameter
    TDZ = 0.0,   # Thread diameter size
    TFLA = 0.0,   # Tap floating length ahead
    TFLB = 0.0,   # Tap floating length behind
    THCHT = 0.0,   # Threading chamfer type
    THFT = 0.0,   # Form type
    THLGTH = 0.0,   # Thread length
    THUB = 0.0,   # Hub thickness
    TP = 0.0,   # Thread pitch
    TPI = 0.0,   # Threads per inch
    TPIN = 0.0,   # Threads per inch minimum
    TPIX = 0.0,   # Threads per inch maximum
    TPN = 0.0,   # Thread pitch minimum
    TPX = 0.0,   # Thread pitch maximum
    TQ = 0.0,   # Torque
    TSYC = 0.0,   # Tool style code
    ULDR = 0.0,   # Usable length diameter ratio
    WB = 0.0,   # Body width
    WF = 0.0,   # Functional width
    WSC = 0.0,   # Clamping width
    WT = 0.0,   # Weight of item
    W1 = 0.0,   # Insert width
    ZEFF = 0.0,   # Face effective cutting edge count
    ZEFP = 0.0,   # Peripheral effective cutting edge count
    ZWX = 0.0   # Number of Wiper inserts maximum
)

cut_params_3 = CutParams(
    ALP = 0.0,   # Clearance angle axial
    ANN = 0.0,   # Clearance angle minor
    APMX = 0.0,  # Depth of cut maximum
    B = 0.0,   # Shank width
    BAWS = 0.0,   # Body angle workpiece side
    BBD = 0.0,   # Balanced by design
    BBR = 0.0,  # Balanced by rotational test
    BD = 0.0,  # Body diameter
    BHTA = 0.0,   # Body half taper angle
    BS = 0.0,   # Wiper edge length
    BSG = 0.0,   # Basic standard group
    CDX = 0.0,   # Cutting depth maximum
    CHW = 0.0,   # Corner chamfer width
    CICT = 0.0,   # Cutting item count
    CND = 0.0,   # Coolant entry diameter
    CNSC = 0.0,   # Coolant entry style code
    COATING = 0.0,   # Coating
    CNT = 0.0,   # Coolant entry thread size
    CP = 0.0,   # Coolant pressure
    CRKS = 0.0,   # Connection retention knob thread size
    CTPT = 0.0,   # Operation type
    CUTDIA = 0.0,   # Work piece parting diameter maximum
    CW = 0.0,   # Cutting width
    CWTOLL = 0.0,   # Cutting width lower tolerance
    CWTOLU = 0.0,   # Cutting width upper tolerance
    CXSC = 0.0,   # Coolant exit style code
    CZC = 0.0,   # Connection size code
    CZC_MS = 0.0,   # Connection size code machine side
    CZC_WS = 0.0,   # Connection size code workpiece side
    DAH = 0.0,   # Diameter access hole
    DAXIN = 0.0,   # Axial groove inside diameter minimum
    DAXX = 0.0,   # Axial groove outside diameter maximum
    DBC = 0.0,   # Diameter bolt circle
    DC = 0.0,   # Cutting diameter
    DCB = 0.0,   # Connection bore diameter
    DCBN = 0.0,   # Connection bore diameter minimum
    DCBX = 0.0,   # Connection bore diameter maximum
    DCF = 0.0,   # Cutting diameter face contact
    DCON = 0.0,   # Connection diameter
    DCSFMS = 0.0,   # Contact surface diameter machine side
    DCSFWS = 0.0,   # Contact surface diameter workpiece side
    DCX = 0.0,   # Maximum cutting diameter
    DIX = 0.0,   # Tool changer interference diameter maximum
    DMIN = 0.0,   # Minimum bore diameter
    DMM = 0.0,   # Shank diameter
    DN = 0.0,   # Neck diameter
    DSGN = 0.0,   # Design
    D1 = 0.0,   # Fixing hole diameter
    FHA = 0.0,   # Flute helix angle
    FLGT = 0.0,   # Flange thickness
    FTDZ = 0.0,   # For thread diameter size
    H = 0.0,  # Shank height
    HF = 0.0,   # Functional height
    HRY = 0.0,   # Lowest point from reference plain
    HTB = 0.0,   # Body height
    HTH = 0.0,   # Height
    IC = 0.0,   # Inscribed circle diameter
    INSL = 0.0,   # Insert length
    IZC = 0.0,   # Insert size code
    KAPR = 0.0,   # Tool cutting edge angle
    KCH = 0.0,   # Corner chamfer
    L = 0.0,   # Cutting edge length
    LB = 0.0,   # Body length
    LCF = 0.0,   # Length chip flute
    LE = 0.0,   # Cutting edge effective length
    LF = 0.0,   # Functional length
    LGR = 0.0,   # Regrind length
    LH = 0.0,   # Head length
    LPR = 0.0,   # Protruding length
    LS = 0.0,   # Shank length
    LSC = 0.0,   # Clamping length
    LSCN = 0.0,   # Clamping length minimum
    LSCX = 0.0,   # Clamping length maximum
    LSD = 0.0,   # Dead shank length
    LU = 0.0,   # Usable length (max. recommended)
    MHD = 0.0,   # Mounting hole distance
    MIID = 0.0,   # Master insert identification
    MMCC = 0.0,   # Code for preset torque
    NOF = 0.0,   # Flute count
    OAH = 0.0,   # Overall height
    OAL = 0.0,   # Overall length
    OAW = 0.0,   # Overall width
    OHN = 0.0,   # Overhang minimum
    OHX = 0.0,   # Overhang maximum
    PHD = 0.0,   # Premachined hole diameter
    PHDX = 0.0,  # Premachined hole diameter maximum
    PL = 0.0,   # Point length
    PRFRAD = 0.0,   # Profile radius
    PRSPC = 0.0,   # Profile specification
    PSIR = 0.0,   # Tool lead angle
    PSIRL = 0.0,   # Cutting edge angle major left hand
    PSIRR  = 0.0,  # Cutting edge angle major right hand
    RADH = 0.0,   # Radial body height
    RADW = 0.0,   # Radial body width
    RE = 0.0,   # Corner radius
    RETOLL = 0.0,   # Corner radius lower tolerance
    RETOLU = 0.0,   # Corner radius upper tolerance
    RPMX = 0.0,   # Rotational speed maximum
    S = 0.0,   # Insert thickness
    SDL = 0.0,   # Step diameter length
    SIG = 0.0,   # Point angle
    SSC = 0.0,   # Insert seat size code
    SUBSTRATE = 0.0,   # Substrate
    TCDC = 0.0,  # Tolerance class cutting diameter
    TCDMM = 0.0,   # Shank diameter tolerance
    TCHA = 0.0,   # Achievable hole tolerance
    TCT = 0.0,   # Tolerance class tool
    TCTR = 0.0,   # Thread tolerance class
    TD = 0.0,   # Thread diameter
    TDZ = 0.0,   # Thread diameter size
    TFLA = 0.0,   # Tap floating length ahead
    TFLB = 0.0,   # Tap floating length behind
    THCHT = 0.0,   # Threading chamfer type
    THFT = 0.0,   # Form type
    THLGTH = 0.0,   # Thread length
    THUB = 0.0,   # Hub thickness
    TP = 0.0,   # Thread pitch
    TPI = 0.0,   # Threads per inch
    TPIN = 0.0,   # Threads per inch minimum
    TPIX = 0.0,   # Threads per inch maximum
    TPN = 0.0,   # Thread pitch minimum
    TPX = 0.0,   # Thread pitch maximum
    TQ = 0.0,   # Torque
    TSYC = 0.0,   # Tool style code
    ULDR = 0.0,   # Usable length diameter ratio
    WB = 0.0,   # Body width
    WF = 0.0,   # Functional width
    WSC = 0.0,   # Clamping width
    WT = 0.0,   # Weight of item
    W1 = 0.0,   # Insert width
    ZEFF = 0.0,   # Face effective cutting edge count
    ZEFP = 0.0,   # Peripheral effective cutting edge count
    ZWX = 0.0   # Number of Wiper inserts maximum
)

################################################
#
# Tool Parameters
#
################################################
tool_1 = Tool(
    remark = "no tool",
    tool_no = 0,
    pocket = 0,
    in_use = 0,
    x_offset = 0.0,
    y_offset = 0.0,
    z_offset = 0.0,
    a_offset = 0.0,
    b_offset = 0.0,
    c_offset = 0.0,
    i_offset = 0.0,
    j_offset = 0.0,
    q_offset = 0.0,
    u_offset = 0.0,
    v_offset = 0.0,
    w_offset = 0.0,
    diameter = 0.0,
    probe_params = [ probe_params_1 ],
    cut_params = [ cut_params_1 ]
)


tool_2 = Tool(
    remark = "Example Tool 1",
    tool_no = 0,
    pocket = 0,
    in_use = 0,
    x_offset = 0.0,
    y_offset = 0.0,
    z_offset = 0.0,
    a_offset = 0.0,
    b_offset = 0.0,
    c_offset = 0.0,
    i_offset = 0.0,
    j_offset = 0.0,
    q_offset = 0.0,
    u_offset = 0.0,
    v_offset = 0.0,
    w_offset = 0.0,
    diameter = 2.0,
    probe_params = [ probe_params_2 ],
    cut_params = [ cut_params_2 ]
)
tool_3 = Tool(
    remark = "Example Tool 2",
    tool_no = 2,
    pocket = 0,
    in_use = 0,
    x_offset = 0.0,
    y_offset = 0.0,
    z_offset = 0.0,
    a_offset = 0.0,
    b_offset = 0.0,
    c_offset = 0.0,
    i_offset = 0.0,
    j_offset = 0.0,
    q_offset = 0.0,
    u_offset = 0.0,
    v_offset = 0.0,
    w_offset = 0.0,
    diameter = 2.0,
    probe_params = [ probe_params_3 ],
    cut_params = [ cut_params_3 ]
)

tool_table = ToolTable(name="Main Tool Table")

# tool_1.probe = [probe_params_1]
# tool_2.probe = [probe_params_2]
# tool_3.probe = [probe_params_3]

tool_table.tools = [tool_1, tool_2, tool_3]

# 9 - persists data
session.add(tool_table)

session.add(tool_1)
session.add(tool_2)
session.add(tool_3)

# 10 - commit and close session
session.commit()
session.close()
