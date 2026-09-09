"""MCP Server for Discrete Wavelet Transform Skill."""
import json
import sys
from client import HaarWaveletTransform

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "dwt_decompose",
                            "description": "Decompose signal using Discrete Wavelet Transform",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "signal": {"type": "array", "items": {"type": "number"}}
                                },
                                "required": ["signal"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                a, d = HaarWaveletTransform.forward(args["signal"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"approx": a, "detail": d})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
