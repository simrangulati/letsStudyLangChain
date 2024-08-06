from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Initialize OpenAI LLM
llm = OpenAI(api_key='your-openai-api-key')

# Set up memory to maintain conversation context
memory = ConversationBufferMemory()

# Create a conversation chain
conversation = ConversationChain(llm=llm, memory=memory)

# Start a conversation
response = conversation.predict("What is the capital of France?")
print(response)  # Output: "The capital of France is Paris."

# Continue the conversation with context retained
response = conversation.predict("And what is its population?")
print(response)  # Output: "The population of Paris is approximately 2.16 million people."
