#!/usr/bin/env ruby
# A script that outputs [sender], [receiver], [flags]


log_content = File.read(ARGV[0])

parsed_entries = log_content.scan(/\[from:(\+\d+)\] \[to:(\+\d+)\] \[flags:(.*?)\]/)

parsed_entries.each do |entry|
  sender = entry[0]
  receiver = entry[1]
  flags = entry[2]
  puts "#{sender},#{receiver},#{flags}"
end
