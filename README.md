# LangChain agent with an agent_utils memory backend

Use the hosted **agent_utils Swarm** server as the persistence layer behind a LangChain
agent's long-term memory - remembered across sessions and machines, no local DB.

## Run

```bash
pip install agent-utils-swarm
AGENT_UTILS_TOKEN=sk_$(openssl rand -hex 32) python example.py
```

The first call auto-provisions a free trial (no card).

## What this demonstrates

`put_memory` / `get_memory` as a durable store you can plug into a LangChain memory class.
The same server also has locks, a task board and pub/sub, and the same token works on the extensions server -
[agent-utils hub](https://github.com/agent-utils/agent-utils).

## License

MIT. agent_utils is a hosted commercial service; this example is not the service.
