import argparse

supported_agents = ['snow', 'rapid7']

def process_report_per_agent(ar, ar2):
    print("supported", ar2)


def main(param):
    agents_param = param.agents

    agents = agents_param.split(",")
    for agent in agents:
        if agent.lower() in supported_agents:
            process_report_per_agent("OUTPUT_FILE", agent)
        else:
            print(f"Agent {agent.capitalize()} is not yet supported..skipping..")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Comma separated list of supported agents.")
    parser.add_argument("--agents", type=str, default="snow,rapid7, opsramp", help="agents")

    args = parser.parse_args()
    main(args)