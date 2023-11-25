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
