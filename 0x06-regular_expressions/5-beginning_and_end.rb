#!/usr/bin/env ruby
# A Script that matches a string that start with h ends with n and can have
# a single character within 

puts ARGV[0].scan(/^h.?n$/)
