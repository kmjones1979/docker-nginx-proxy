class WelcomeController < ApplicationController
  def index
    self.request.env.each do |header|
      response.stream.write "#{header[0]}: #{header[1]} \n"
    end
  end
end
