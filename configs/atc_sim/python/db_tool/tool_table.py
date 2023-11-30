# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey, Float, Text
from sqlalchemy.orm import relationship

from base import Base


class ToolTable(Base):
    __tablename__ = 'tool_table'

    id = Column(Integer, primary_key=True)
    
    name = Column(String)
    description = Column(String)
    
    
    tools = relationship("Tool")

        
class Tool(Base):
    __tablename__ = 'tool'
    
    id = Column(Integer, primary_key=True)
    
    remark = Column(Text)
    tool_no = Column(Integer)
    in_use = Column(Integer)
    pocket = Column(Integer)
    
    x_offset = Column(Float)
    y_offset = Column(Float)
    z_offset = Column(Float)
    a_offset = Column(Float)
    b_offset = Column(Float)
    c_offset = Column(Float)
    i_offset = Column(Float)
    j_offset = Column(Float)
    q_offset = Column(Float)
    u_offset = Column(Float)
    v_offset = Column(Float)
    w_offset = Column(Float)
    diameter = Column(Float)
    
    probe_params = relationship("ProbeParams")
    cut_params = relationship("CutParams")
    
    tool_table = relationship("ToolTable", back_populates="tools")
    tool_table_id = Column(Integer, ForeignKey('tool_table.id'))

class ProbeParams(Base):
    __tablename__ = 'probe_params'
    
    id = Column(Integer, primary_key=True)
    
    tool_id = Column(Integer, ForeignKey('tool.id'))
    
    tool_table = relationship("Tool", back_populates="probe_params")
    
    tool_diameter_probe_mode = Column(Text)
    tool_diameter_offset_mode = Column(Text)
    tool_diameter = Column(Text)
    tool_breakage_detection_mode = Column(Text)
    tool_breakage_tolerance = Column(Text)
    
    
class CutParameters(Base):
    __tablename__ = 'cut_parameters'
    
    id = Column(Integer, primary_key=True)
    
    tool_id = Column(Integer, ForeignKey('tool.id'))
    tool_table = relationship("Tool", back_populates="cut_params")
    
    
    ALP = Column(Float)   # Clearance angle axial
    ANN = Column(Float)   # Clearance angle minor
    APMX = Column(Float)  # Depth of cut maximum
    B = Column(Float)   # Shank width
    BAWS = Column(Float)   # Body angle workpiece side
    BBD = Column(Float)   # Balanced by design
    BBR = Column(Float)  # Balanced by rotational test
    BD = Column(Float)  # Body diameter
    BHTA = Column(Float)   # Body half taper angle
    BS = Column(Float)   # Wiper edge length
    BSG = Column(Float)   # Basic standard group
    CDX = Column(Float)   # Cutting depth maximum
    CHW = Column(Float)   # Corner chamfer width
    CICT = Column(Float)   # Cutting item count
    CND = Column(Float)   # Coolant entry diameter
    CNSC = Column(Float)   # Coolant entry style code
    COATING = Column(Float)   # Coating
    CNT = Column(Float)   # Coolant entry thread size
    CP = Column(Float)   # Coolant pressure
    CRKS = Column(Float)   # Connection retention knob thread size
    CTPT = Column(Float)   # Operation type
    CUTDIA = Column(Float)   # Work piece parting diameter maximum
    CW = Column(Float)   # Cutting width
    CWTOLL = Column(Float)   # Cutting width lower tolerance
    CWTOLU = Column(Float)   # Cutting width upper tolerance
    CXSC = Column(Float)   # Coolant exit style code
    CZC = Column(Float)   # Connection size code
    CZC_MS = Column(Float)   # Connection size code machine side
    CZC_WS = Column(Float)   # Connection size code workpiece side
    DAH = Column(Float)   # Diameter access hole
    DAXIN = Column(Float)   # Axial groove inside diameter minimum
    DAXX = Column(Float)   # Axial groove outside diameter maximum
    DBC = Column(Float)   # Diameter bolt circle
    DC = Column(Float)   # Cutting diameter
    DCB = Column(Float)   # Connection bore diameter
    DCBN = Column(Float)   # Connection bore diameter minimum
    DCBX = Column(Float)   # Connection bore diameter maximum
    DCF = Column(Float)   # Cutting diameter face contact
    DCON = Column(Float)   # Connection diameter
    DCSFMS = Column(Float)   # Contact surface diameter machine side
    DCSFWS = Column(Float)   # Contact surface diameter workpiece side
    DCX = Column(Float)   # Maximum cutting diameter
    DIX = Column(Float)   # Tool changer interference diameter maximum
    DMIN = Column(Float)   # Minimum bore diameter
    DMM = Column(Float)   # Shank diameter
    DN = Column(Float)   # Neck diameter
    DSGN = Column(Float)   # Design
    D1 = Column(Float)   # Fixing hole diameter
    FHA = Column(Float)   # Flute helix angle
    FLGT = Column(Float)   # Flange thickness
    FTDZ = Column(Float)   # For thread diameter size
    H = Column(Float)  # Shank height
    HF = Column(Float)   # Functional height
    HRY = Column(Float)   # Lowest point from reference plain
    HTB = Column(Float)   # Body height
    HTH = Column(Float)   # Height
    IC = Column(Float)   # Inscribed circle diameter
    INSL = Column(Float)   # Insert length
    IZC = Column(Float)   # Insert size code
    KAPR = Column(Float)   # Tool cutting edge angle
    KCH = Column(Float)   # Corner chamfer
    L = Column(Float)   # Cutting edge length
    LB = Column(Float)   # Body length
    LCF = Column(Float)   # Length chip flute
    LE = Column(Float)   # Cutting edge effective length
    LF = Column(Float)   # Functional length
    LGR = Column(Float)   # Regrind length
    LH = Column(Float)   # Head length
    LPR = Column(Float)   # Protruding length
    LS = Column(Float)   # Shank length
    LSC = Column(Float)   # Clamping length
    LSCN = Column(Float)   # Clamping length minimum
    LSCX = Column(Float)   # Clamping length maximum
    LSD = Column(Float)   # Dead shank length
    LU = Column(Float)   # Usable length (max. recommended)
    MHD = Column(Float)   # Mounting hole distance
    MIID = Column(Float)   # Master insert identification
    MMCC = Column(Float)   # Code for preset torque
    NOF = Column(Float)   # Flute count
    OAH = Column(Float)   # Overall height
    OAL = Column(Float)   # Overall length
    OAW = Column(Float)   # Overall width
    OHN = Column(Float)   # Overhang minimum
    OHX = Column(Float)   # Overhang maximum
    PHD = Column(Float)   # Premachined hole diameter
    PHDX = Column(Float)  # Premachined hole diameter maximum
    PL = Column(Float)   # Point length
    PRFRAD = Column(Float)   # Profile radius
    PRSPC = Column(Float)   # Profile specification
    PSIR = Column(Float)   # Tool lead angle
    PSIRL = Column(Float)   # Cutting edge angle major left hand
    PSIRR  = Column(Float)  # Cutting edge angle major right hand
    RADH = Column(Float)   # Radial body height
    RADW = Column(Float)   # Radial body width
    RE = Column(Float)   # Corner radius
    RETOLL = Column(Float)   # Corner radius lower tolerance
    RETOLU = Column(Float)   # Corner radius upper tolerance
    RPMX = Column(Float)   # Rotational speed maximum
    S = Column(Float)   # Insert thickness
    SDL = Column(Float)   # Step diameter length
    SIG = Column(Float)   # Point angle
    SSC = Column(Float)   # Insert seat size code
    SUBSTRATE = Column(Float)   # Substrate
    TCDC = Column(Float)  # Tolerance class cutting diameter
    TCDMM = Column(Float)   # Shank diameter tolerance
    TCHA = Column(Float)   # Achievable hole tolerance
    TCT = Column(Float)   # Tolerance class tool
    TCTR = Column(Float)   # Thread tolerance class
    TD = Column(Float)   # Thread diameter
    TDZ = Column(Float)   # Thread diameter size
    TFLA = Column(Float)   # Tap floating length ahead
    TFLB = Column(Float)   # Tap floating length behind
    THCHT = Column(Float)   # Threading chamfer type
    THFT = Column(Float)   # Form type
    THLGTH = Column(Float)   # Thread length
    THUB = Column(Float)   # Hub thickness
    TP = Column(Float)   # Thread pitch
    TPI = Column(Float)   # Threads per inch
    TPIN = Column(Float)   # Threads per inch minimum
    TPIX = Column(Float)   # Threads per inch maximum
    TPN = Column(Float)   # Thread pitch minimum
    TPX = Column(Float)   # Thread pitch maximum
    TQ = Column(Float)   # Torque
    TSYC = Column(Float)   # Tool style code
    ULDR = Column(Float)   # Usable length diameter ratio
    WB = Column(Float)   # Body width
    WF = Column(Float)   # Functional width
    WSC = Column(Float)   # Clamping width
    WT = Column(Float)   # Weight of item
    W1 = Column(Float)   # Insert width
    ZEFF = Column(Float)   # Face effective cutting edge count
    ZEFP = Column(Float)   # Peripheral effective cutting edge count
    ZWX = Column(Float)   # Number of Wiper inserts maximum
    
    