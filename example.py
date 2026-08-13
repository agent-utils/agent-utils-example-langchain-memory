"""Back an agent's long-term memory with the hosted agent_utils Memory service.

Run:  AGENT_UTILS_TOKEN=sk_... python example.py
Uses the agent-utils-memory client (pip install agent-utils-memory).
"""

import os
import json
from agent_utils.memory import AgentUtilsMemory

memory = AgentUtilsMemory(token=os.environ["AGENT_UTILS_TOKEN"])

# Persist a fact learned this session; recall it in any future session.
memory.put_memory("user", "prefers", json.dumps("concise answers"), tags=["preference"])
print("stored. recall ->", memory.get_memory("user", "prefers"))

# Wire into LangChain by calling these get/put methods from a custom
# BaseChatMessageHistory / memory class - the store is the agent_utils service.
