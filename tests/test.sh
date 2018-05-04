#!/usr/local/bin/fish

# Create files from tests
for test in *.sexp

  ruby   ../htmlforever.rb (echo (cat $test)) >> ../all-funcs-ruby.html
  node   ../htmlforever.js (echo (cat $test)) >> ../all-funcs-node.html
  python ../htmlforever.py (echo (cat $test)) >> ../all-funcs-python.html

end

# Diff output
diff -B ../all-funcs-node.html ../all-funcs-python.html
diff -B ../all-funcs-node.html ../all-funcs-ruby.html

# Remove test files
rm ../all-funcs-ruby.html ../all-funcs-node.html ../all-funcs-python.html