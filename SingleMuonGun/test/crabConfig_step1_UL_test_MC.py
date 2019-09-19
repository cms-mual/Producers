from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'singleMuonGun_10_6_0_UL_realistic_2M' #name here'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'singleMuonGun_10X_2018_UL_realisitc.py'


config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 2000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publishDBS = 'phys03'
config.Data.outputPrimaryDataset = 'singleMuonGun_10_6_0_UL_realistic_2M'
config.Data.publication = True
#config.Data.outputDatasetTag = 'singleMuonGun_test_tf2_randomness' #name here'
config.Data.outLFNDirBase = '/store/group/alca_muonalign/'

config.section_("Site")
#config.Site.storageSite = 'T3_US_TAMU'
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = [ 'T2_CH_CERN' ]
