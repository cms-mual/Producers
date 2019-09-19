from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = '_UL_MC_realistic_step2' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.psetName = 'singleMuonGun__10X_2018_UL_realisitc_RAW2DIGI_RECO.py'
config.JobType.pluginName = 'Analysis'



config.section_("Data")
config.Data.inputDBS = 'phys03'
#config.Data.inputDataset = '/singleMuonGun_10_6_0_design_25m_2018_step1/adthomps-crab_singleMuonGun_10_6_0_design_25m_2018_step1-161852546f2166086facece91ca7d907/USER'
#config.Data.inputDataset = '/singleMuonGun_10_6_0_design_25m_2018_step1/rymuelle-crab_singleMuonGun_10_6_0_design_25m_2018_step1-f7e65314c42d495bb2bd1d8d644f2e7a/USER'
config.Data.inputDataset = '/singleMuonGun_10_6_0_UL_realistic/rymuelle-crab_singleMuonGun_10_6_0_UL_realistic-5c98b8f5550acb7e6ed0b2d1796e0990/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
#NJOBS = 9000
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.publishDBS = 'phys03'
#config.Data.outputPrimaryDataset = 'singleMuonGun_10_1_0_pre3_realistic_ideal_22p5M_2018_ideal_step2_ALCARECO'
config.Data.publication = False
#config.Data.outputDatasetTag = 'singleMuonGun_test_tf2_randomness' #name here'
config.Data.outLFNDirBase = '/store/group/alca_muonalign/'

config.section_("Site")
#config.Site.storageSite = 'T3_US_TAMU'
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = [ 'T2_CH_CERN' ]
