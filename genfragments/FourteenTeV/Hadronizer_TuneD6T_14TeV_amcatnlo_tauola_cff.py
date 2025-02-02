import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUESettings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia6HadronizerFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    comEnergy = cms.double(14000.0),
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=0         ! User defined processes', 
                        'PMAS(5,1)=4.8   ! b quark mass',
                        'PMAS(6,1)=172.5 ! t quark mass',
			'MSTJ(1)=1       ! Fragmentation/hadronization on or off',
			'MSTP(61)=1      ! Parton showering on or off',
                         # aMCatNLO parameters
                        'MSTJ(43) = 3 !',
                        'MSTJ(47) = 0 !',
                        'MSTJ(48) = 0 !',
                        'MSTJ(50) = 2 !',
                        'MSTJ(67) = 2 !',
                        'MSTJ(68) = 0 !',
                        'PARP(67) = 1 !',
                        'PARP(71) = 1 !'),
                        # This is a vector of ParameterSet names to be read, in this order                     
                         parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)
