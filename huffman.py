import heapq
from collections import Counter, defaultdict
import os

class HuffmanNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(symbol_freq):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in symbol_freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(node, code=""):
    if node is None:
        return {}
    if node.symbol is not None:
        return {node.symbol: code}
    
    codes = {}
    codes.update(generate_huffman_codes(node.left, code + "0"))
    codes.update(generate_huffman_codes(node.right, code + "1"))
    return codes

def calculate_avg_codeword_length(symbol_freq, huffman_codes):
    total_weighted_length = 0
    total_frequency = sum(symbol_freq.values())
    
    for symbol, freq in symbol_freq.items():
        total_weighted_length += freq * len(huffman_codes[symbol])
    
    return total_weighted_length / total_frequency

def huffman_encoding(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    symbol_freq = Counter(data)
    
    root = build_huffman_tree(symbol_freq)
    huffman_codes = generate_huffman_codes(root)
    
    print("Codeword Table:")
    for symbol, code in sorted(huffman_codes.items()):
        print(f"Byte: {symbol:3} Code: {code}")
    
    avg_length = calculate_avg_codeword_length(symbol_freq, huffman_codes)
    print(f"\nAverage Codeword Length: {avg_length:.2f}")

file_path ="englishText.txt"
huffman_encoding(file_path)
