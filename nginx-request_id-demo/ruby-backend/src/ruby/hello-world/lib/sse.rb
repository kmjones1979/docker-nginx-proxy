require 'json'

module ServerSide
  class SSE
    def initialize io
      @io = io
    end

    def write object, options = {}
      options.each do |k,v|
        @io.write "#{k}: #{v}"
      end
      @io.write "#{object}\n"
    end

    def close
      @io.close
    end
  end
end
