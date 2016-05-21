require 'json'
require 'sse'

class WelcomeController < ApplicationController

  def index
    response.headers['Content-Type'] = 'text/event-stream'
    sse = ServerSide::SSE.new(response.stream)
    begin
      request.env.each do |header|
        sse.write("#{header[0]}: " "#{header[1]}")
        # create log line here with join
      end
    rescue IOError
    ensure
      sse.close
    end
  end

end
