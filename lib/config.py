from easydict import EasyDict as edict

cfg = edict()

cfg.GENERAL = edict()
cfg.GENERAL.MIN_IMG_RATIO = 0.5
cfg.GENERAL.MAX_IMG_RATIO = 2.0
cfg.GENERAL.MIN_IMG_SIZE = 600
cfg.GENERAL.MAX_IMG_SIZE = 1000
cfg.GENERAL.POOLING_MODE = 'pool'
cfg.GENERAL.POOLING_SIZE = 7

cfg.TRAIN = edict()
cfg.TRAIN.BATCH_SIZE = 1
cfg.TRAIN.LEARNING_RATE = 0.001
cfg.TRAIN.LR_DECAY_STEP = 5
cfg.TRAIN.LR_DECAY_GAMMA = 0.1
cfg.TRAIN.MOMENTUM = 0.9
cfg.TRAIN.DOUBLE_BIAS = True
cfg.TRAIN.BIAS_DECAY = False
cfg.TRAIN.WEIGHT_DECAY = 0.0005

cfg.TRAIN.RPN_PRE_NMS_TOP = 12000
cfg.TRAIN.RPN_POST_NMS_TOP = 2000
cfg.TRAIN.RPN_NMS_THRESHOLD = 0.7
# If an anchor statisfied by positive and negative conditions set to negative
cfg.TRAIN.RPN_CLOBBER_POSITIVES = False
cfg.TRAIN.RPN_NEGATIVE_OVERLAP = 0.3
cfg.TRAIN.RPN_POSITIVE_OVERLAP = 0.7
cfg.TRAIN.RPN_MAX_LABELS = 256
cfg.TRAIN.RPN_FG_LABELS_FRACTION = 0.5

cfg.TRAIN.USE_FLIPPED = True
cfg.TRAIN.PROPOSAL_PER_IMG = 256
cfg.TRAIN.FG_PROPOSAL_FRACTION = 0.25
cfg.TRAIN.FG_THRESHOLD = 0.5
cfg.TRAIN.BG_THRESHOLD_HI = 0.5
cfg.TRAIN.BG_THRESHOLD_LO = 0.0

cfg.RPN = edict()
cfg.RPN.ANCHOR_SCALES = [8, 16, 32]
cfg.RPN.ANCHOR_RATIOS = [0.5, 1, 2]
cfg.RPN.FEATURE_STRIDE = 16

cfg.TEST = edict()
cfg.TEST.RPN_PRE_NMS_TOP = 6000
cfg.TEST.RPN_POST_NMS_TOP = 300
cfg.TEST.RPN_NMS_THRESHOLD = 0.7
cfg.TEST.NMS = 0.3

cfg.RESNET = edict()
cfg.RESNET.NUM_FREEZE_BLOCKS = 1
