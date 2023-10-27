#!/usr/bin/env python3
class DNARecord(object):
  def __init__(self, name,sequence,organism):
    self.name=name
    self.sequence=sequence
    self.organism= organism
    name= 'ABC1'
    sequence= 'ATGGTTGACGTGACGTGTT'
    organism= 'human'

dna_rec_obj=DNARecord()
print( dna_rec_obj.name, dna_rec_obj.sequence,dna_rec_obj.organism)

