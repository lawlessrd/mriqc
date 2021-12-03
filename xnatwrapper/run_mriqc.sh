#!/bin/bash

### Script for mriqc docker container
# Dylan Lawless
# Usage: run_mriqc: [--bidsdir] [--outdir] [--wrkdir] [--label_info]


# Initialize defaults
export bidsdir=NO_BIDS
export outdir=NO_OUTDIR
export level=participant
export project=NO_PROJECT
export subject=NO_SUBJECT
export session=NO_SESSION
export scan=NO_SCAN

# Parse options
while [[ $# -gt 0 ]]; do
  key="${1}"
  case $key in
    --bidsdir)
      export bidsdir="${2}"; shift; shift ;;
    --outdir)
      export outdir="${2}"; shift; shift ;;
    --project)
      export project="${2}"; shift; shift ;;
    --subject)
      export subject="${2}"; shift; shift ;;
    --session)
      export session="${2}"; shift; shift ;;
    --scan)
      export scan="${2}"; shift; shift ;;
    *)
      echo Unknown input "${1}"; shift ;;
  esac
done

#Run MRIQC
mriqc --no-sub ${bidsdir} ${outdir} ${level} 

#Convert outputs
cd ${outdir}

#Run py scripts to convert outputs
/opt/xnatwrapper/convert_outputs.py
