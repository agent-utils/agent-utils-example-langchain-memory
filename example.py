"""Back an agent's long-term memory with the hosted agent_utils Swarm server.

Run:  AGENT_UTILS_TOKEN=sk_... python example.py
Uses the agent-utils-swarm client (pip install agent-utils-swarm).
"""

import os
import json
from agent_utils.swarm import AgentUtilsSwarm

memory = AgentUtilsSwarm(token=os.environ["AGENT_UTILS_TOKEN"])


def recall(namespace, key):
    """Return the stored value, or None. Tool results arrive as MCP text content."""
    result = json.loads(memory.get_memory(namespace, key)["content"][0]["text"])
    return json.loads(result["value_json"]) if result.get("exists") else None


# Persist a fact learned this session; recall it in any future session.
memory.put_memory("user", "prefers", json.dumps("concise answers"), tags=["preference"])
print("stored. recall ->", recall("user", "prefers"))

# Wire into LangChain by calling these get/put methods from a custom
# BaseChatMessageHistory / memory class - the store is the agent_utils service.
