{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue247;\red23\green24\blue24;\red202\green202\blue202;
\red109\green115\blue120;\red212\green212\blue212;\red113\green192\blue131;\red246\green124\blue48;}
{\*\expandedcolortbl;;\cssrgb\c77255\c54118\c97647;\cssrgb\c11765\c12157\c12549;\cssrgb\c83137\c83137\c83137;
\cssrgb\c50196\c52549\c54510;\cssrgb\c86275\c86275\c86275;\cssrgb\c50588\c78824\c58431;\cssrgb\c98039\c56471\c24314;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  random\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  string\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  time\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Dictionary to map screen size choice to the blocks to generate per line\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # 1080p: The original 13 blocks\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # 2K: 20 blocks\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # 4K: 30 blocks\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 BLOCK_COUNTS = \cf6 \strokec6 \{\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 '1080p'\cf6 \strokec6 :\cf4 \strokec4  \cf8 \strokec8 13\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 '2k'\cf6 \strokec6 :\cf4 \strokec4  \cf8 \strokec8 20\cf6 \strokec6 ,\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 '4k'\cf6 \strokec6 :\cf4 \strokec4  \cf8 \strokec8 30\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 \}\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  get_block_count\cf6 \strokec6 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 print\cf6 \strokec6 (\cf7 \strokec7 "\\nSelect an output density (Screen Size):"\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 print\cf6 \strokec6 (\cf7 \strokec7 "  1. 1080p (13 blocks per line - Standard)"\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 print\cf6 \strokec6 (\cf7 \strokec7 "  2. 2K (20 blocks per line - Higher density)"\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 print\cf6 \strokec6 (\cf7 \strokec7 "  3. 4K (30 blocks per line - Very high density)"\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 while\cf4 \strokec4  \cf2 \strokec2 True\cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3         choice = \cf2 \strokec2 input\cf6 \strokec6 (\cf7 \strokec7 "Enter your choice (1, 2, 3, 1080p, 2k, or 4k): "\cf6 \strokec6 )\cf4 \strokec4 .lower\cf6 \strokec6 ()\cf4 \strokec4 .strip\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\cb3         \cb1 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  choice \cf2 \strokec2 in\cf4 \strokec4  \cf6 \strokec6 [\cf7 \strokec7 '1'\cf6 \strokec6 ,\cf4 \strokec4  \cf7 \strokec7 '1080p'\cf6 \strokec6 ]:\cf4 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 return\cf4 \strokec4  BLOCK_COUNTS\cf6 \strokec6 [\cf7 \strokec7 '1080p'\cf6 \strokec6 ]\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 elif\cf4 \strokec4  choice \cf2 \strokec2 in\cf4 \strokec4  \cf6 \strokec6 [\cf7 \strokec7 '2'\cf6 \strokec6 ,\cf4 \strokec4  \cf7 \strokec7 '2k'\cf6 \strokec6 ]:\cf4 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 return\cf4 \strokec4  BLOCK_COUNTS\cf6 \strokec6 [\cf7 \strokec7 '2k'\cf6 \strokec6 ]\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 elif\cf4 \strokec4  choice \cf2 \strokec2 in\cf4 \strokec4  \cf6 \strokec6 [\cf7 \strokec7 '3'\cf6 \strokec6 ,\cf4 \strokec4  \cf7 \strokec7 '4k'\cf6 \strokec6 ]:\cf4 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 return\cf4 \strokec4  BLOCK_COUNTS\cf6 \strokec6 [\cf7 \strokec7 '4k'\cf6 \strokec6 ]\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 else\cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 print\cf6 \strokec6 (\cf7 \strokec7 "Invalid choice. Please enter 1, 2, 3, 1080p, 2k, or 4k."\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  letterprint\cf6 \strokec6 (\cf4 \strokec4 num_blocks\cf6 \strokec6 ):\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 print\cf6 \strokec6 (\cf7 \strokec7 f"\\n--- Generating \cf4 \strokec4 \{num_blocks\}\cf7 \strokec7  blocks per line. Press Ctrl+C to stop. ---"\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 while\cf4 \strokec4  \cf2 \strokec2 True\cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 # number of blocks using a list compression\cf4 \cb1 \strokec4 \
\cb3         \cf5 \strokec5 # shuffled string of alphabet letters\cf4 \cb1 \strokec4 \
\cb3         blocks = \cf6 \strokec6 [\cf4 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 ''\cf4 \strokec4 .join\cf6 \strokec6 (\cf4 \strokec4 random.sample\cf6 \strokec6 (\cf4 \strokec4 string.ascii_lowercase\cf6 \strokec6 ,\cf4 \strokec4  \cf8 \strokec8 26\cf6 \strokec6 ))\cf4 \strokec4  \cb1 \
\cb3             \cf2 \strokec2 for\cf4 \strokec4  \cf2 \strokec2 _\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf2 \strokec2 range\cf6 \strokec6 (\cf4 \strokec4 num_blocks\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3         \cf6 \strokec6 ]\cf4 \cb1 \strokec4 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 # Print all blocks separated by spaces\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 print\cf6 \strokec6 (\cf4 \strokec4 *blocks\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3         \cb1 \
\cb3         sleep\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  sleep\cf6 \strokec6 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     time.sleep\cf6 \strokec6 (\cf8 \strokec8 0.3\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf4 \strokec4  main\cf6 \strokec6 ():\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     block_count = get_block_count\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 try\cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3         letterprint\cf6 \strokec6 (\cf4 \strokec4 block_count\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 except\cf4 \strokec4  KeyboardInterrupt\cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 print\cf6 \strokec6 (\cf7 \strokec7 "\\nProgram terminated by user."\cf6 \strokec6 )\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf2 \strokec2 __name__\cf4 \strokec4  == \cf7 \strokec7 "__main__"\cf6 \strokec6 :\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     main\cf6 \strokec6 ()\cf4 \cb1 \strokec4 \
}