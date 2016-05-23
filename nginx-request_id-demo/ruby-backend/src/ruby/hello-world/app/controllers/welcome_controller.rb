require 'json'
require 'sse'

class WelcomeController < ApplicationController

  def http_logger
    @@http_logger ||= Logger.new("/var/log/ruby/ruby.log")
  end

  def index
    response.headers['Content-Type'] = 'text/event-stream'
    sse = ServerSide::SSE.new(response.stream)
    begin
      request.env.each do |header|
	if header[0] =~ /^(REQUEST_|PATH_|QUERY_|REMOTE_|SERVER_|SCRIPT_|ORIGINAL_|HTTP_)(.*)/
          sse.write("#{header[0]}: " "#{header[1]}")
	  http_logger.info("#{header[0]}: " "#{header[1]}").join("\n")
	end
      end
    rescue IOError
    ensure
      sse.close
    end

  end

end
