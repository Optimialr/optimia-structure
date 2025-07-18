#!/usr/bin/env python3
"""Infrastructure IA - Script de d√©marrage"""
import subprocess
import sys

def main():
    print("Ì∫Ä D√©marrage Infrastructure IA")
    try:
        subprocess.run(["docker", "compose", "up", "-d"], check=True)
        print("‚úÖ Services d√©marr√©s!")
        print("ÔøΩÔøΩ n8n: http://localhost:5678")
        print("Ì¥ç Qdrant: http://localhost:6333") 
        print("Ì¥ñ Ollama: http://localhost:11434")
        print("Ì≥ã Baserow: http://localhost:8080")
    except Exception as e:
        print(f"‚ùå Erreur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
