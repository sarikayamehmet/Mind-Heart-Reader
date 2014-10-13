# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Hassan"
__date__ ="$Oct 2, 2014 1:49:14 PM$"


from app.mhreader import mhrbp
from .. import db
from sqlalchemy import Column, Integer, String, Float, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime, date

class ExperimentFile(db.Model):
    __tablename__ = "mhreader_experiment_files"
    __name__='experiment_set_file'
    id = Column(Integer, primary_key=True)
#    experiment_set_id = Column(Integer, ForeignKey('mhreader_experiment_sets.id'))
    stimulus_type= Column(String)
    title = Column(String)
    filename = Column(String)
    filepath = Column(String)
    file_set_number = Column(Integer)
    remarks = Column(String)
#    experiment_logs = relationship('ExperimentLog', backref=backref('experiment_file'))
    metrics= relationship('ExperimentFileMetric', backref=backref('experiment_file'), cascade= 'delete')
    experiment_set_file= relationship('ExperimentSetFile', backref=backref('experiment_file'), cascade= 'delete')
    
    def __init__(self, stimulus_type, title, filename, filepath='', \
    file_set_number = 0, remarks =''):
        self.stimulus_type=stimulus_type
        self.title=title
        self.filename = filename
        self.filepath = filepath
        self.file_set_number = file_set_number
        self.remarks=remarks
        
    def __repr__(self):
        return '''{"%s":
                    {"id":%d,  
                    "stimulus_type":"%s", 
                    "title":"%s", 
                    "filename":"%s", 
                    "filepath":"%s", 
                    "file_set_number":%d,
                    "remarks":"%s",
                    "metrics":%s}}'''\
                    % (self.__name__,
                    self.id,  
                    self.stimulus_type, 
                    self.title,
                    self.filename,
                    self.filepath,
                    self.file_set_number,
                    self.remarks,
                    [metric for metric in self.metrics]) 
    