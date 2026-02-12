This folder contains the ttl files with some  filtering to remove non-relevant files ie files that do not contain ui:Form definitions


grep -rl "ui:Form" ./ttl | xargs -I{} cp {} ./ttl-filtered
grep -rl ":Form" ./ttl | xargs -I{} cp {} ./ttl-filtered 