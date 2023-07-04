#!/usr/bin/env ruby
data = /from:(?<from>.*?)\]\s\[to:(?<to>.*?)\]\s\[flags:(?<flags>.*?)\]/.match(ARGV[0])
puts "#{data['from']},#{data['to']},#{data['flags']}"
