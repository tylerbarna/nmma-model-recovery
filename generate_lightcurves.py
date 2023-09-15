import os 


models_to_fit = ['nugent-hyper', 'Bu2019lm', 'TrPi2018']
priors_directory = './priors/'
num_lightcurves = 100
filters=['ztfg', 'ztfr', 'ztfi']

outdir = './lightcurves/'

os.makedirs(outdir, exist_ok=True)

for model in models_to_fit:
   inj_path = os.path.join(outdir,'inj_' + model + '.json')
   cmd_str = ['nmma_create_injection',
               '--prior-file', os.path.join(priors_directory, model + '.prior'),
               '-f', inj_path,
               '-e', 'json',
                '-n', str(num_lightcurves),
                '--original-parameters',
                '--eos-file ../nmma/example_files/eos/ALF2.dat', 
                '--binary-type BNS',
               ]
   os.system(' '.join(cmd_str))
    
   cmd_str_2 = ['light_curve_generation',
               '--injection', inj_path,
               '--label', model,
               '--model', model,
               '--svd-path', '../nmma/svdmodels',
               '--tmin', '0.0001',
               '--tmax', '14.5',
               '--dt', '0.5',
               '--ztf-uncertainties',
            #    '--ztf-sampling',
            #    '--ztf-ToO', '300',
               '--filters', ','.join(filters),
               '--outdir', outdir,
               #'--injection-detection-limit', '21.5',
               '--outfile-type', 'json',
               ]
   os.system(' '.join(cmd_str_2))
                 