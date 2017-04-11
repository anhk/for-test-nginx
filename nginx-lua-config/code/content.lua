

local http_lib = require 'resty.http'

local sock = http_lib:new()
local c, err = sock:connect("127.0.0.1", 770)
if not c then
    log(ERR, "Can not connect to 127.0.0.1:770: ", err)
    ngx.exit(502)
end

local res, err = sock:proxy_request()
if not res then
    log(ERR, "Proxy request to 127.0.0.1:770 error: ", err)
    ngx.exit(502)
end

sock:proxy_response(res)
