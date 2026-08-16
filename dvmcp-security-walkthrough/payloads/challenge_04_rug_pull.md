Tool: get_weather
No special payload - just call it more than 3 times in the same session.

1. get_weather(location="London")   -> normal
2. get_weather(location="New York") -> normal
3. get_weather(location="Paris")    -> normal
4. get_weather(location="Tokyo")    -> rug pull triggers
5. get_weather(location="Lagos")    -> still rug-pulled

Behavior flips after state["weather_tool_calls"] > 3.
