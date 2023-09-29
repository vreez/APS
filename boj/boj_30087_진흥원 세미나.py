import sys; sys.stdin = open("30087.txt", "r")
info = {
    "Algorithm":204, "DataAnalysis":207, "ArtificialIntelligence":302,
    "CyberSecurity":"B101", "Network":303, "Startup":501, "TestStrategy":105
}
N = int(input())
for i in range(N):
    s = input()
    print(info[s])
