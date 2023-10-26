#!/usr/bin/env ruby
# A script that search for htn and hbtn 

puts ARGV[0].scan(/hbt{2,5}/).join
