require 'json'
require 'sse'
require 'time'

class WelcomeController < ApplicationController

  def http_logger
    @@http_logger ||= Logger.new("/var/log/ruby/ruby.log")
  end

  def index
    response.headers['Content-Type'] = 'text/event-stream'
    sse = ServerSide::SSE.new(response.stream)
    begin
      http_logger.info "HTTP REQUEST START"
      http_logger << Time.now.iso8601
      request.env.each do |header|
	if header[0] =~ /^(REQUEST_|PATH_|QUERY_|REMOTE_|SERVER_|SCRIPT_|ORIGINAL_|HTTP_)(.*)/
          sse.write("#{header[0]}: " "#{header[1]}")
	  http_logger << " #{header[0]}: " "#{header[1]}"
	end
      end
      http_logger << "\n"
      http_logger.info "HTTP REQUEST END"
    rescue IOError
    ensure
      sse.close
    end

  end

end
