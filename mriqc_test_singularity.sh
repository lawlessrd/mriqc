#!/bin/bash

singularity run \
--cleanenv \
--contain \
--home $(pwd -P) \
--bind $(pwd -P)/BIDS/Nifti:/data \
--bind $(pwd -P)/OUTPUTS:/out \
mriqc_v1.simg \
--bidsdir $(pwd -P)/BIDS/Nifti \
--outdir $(pwd -P)/OUTPUTS \
--project "project" \
--subject "subject" \
--session "session" \
--scan "scan"