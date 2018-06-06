import os

#TECH SPECS
fps = os.environ["fps"]
par = os.environ["par"]
source = os.environ["source"]

#DAILY SPECS
enable_slate = os.environ["enable_slate"]
normalize_framerange = os.environ["normalize_framerange"]


#OUTPUT SPECS
format = os.environ["format"]
codec = os.environ["codec"]





#filepath = "Z:\\territory\\JAUNT_360\\COPA90_DestinationUnited_45_01-rec15972_v02-mono.mov"
filepath = "Z:\\territory\\JAUNT_360\\COPA90_DestinationUnited_51_01-rec15978-clp17604_v03-highquality-mono_prores_hq.mov"

filepath = os.path.normpath(filepath)
filepath = filepath.replace("\\","//")

os.environ["SOURCE"] = filepath

sourceRead.filename.setValue(os.environ["SOURCE"])


## OUTPUT
writeOutput.filename.setValue(output_filename)
writeOutput.codec.setValue(output_codec)