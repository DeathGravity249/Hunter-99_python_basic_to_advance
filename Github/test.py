<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SignSpeak AI - FPGA Sign Language Translator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/feather-icons"></script>
    <script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.globe.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc;
        }
        .gradient-bg {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .wave-animation {
            animation: wave 2s infinite;
        }
        @keyframes wave {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(5deg); }
            75% { transform: rotate(-5deg); }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="bg-white shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <div class="flex-shrink-0 flex items-center">
                        <i data-feather="cpu" class="h-8 w-8 text-indigo-600"></i>
                        <span class="ml-2 text-xl font-bold text-gray-900">SignSpeak AI</span>
                    </div>
                </div>
                <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
                    <a href="#" class="border-indigo-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">Home</a>
                    <a href="#" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">How it works</a>
                    <a href="#" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">Demo</a>
                    <a href="#" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">About</a>
                </div>
                <div class="-mr-2 flex items-center sm:hidden">
                    <button type="button" class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
                        <i data-feather="menu" class="block h-6 w-6"></i>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <div id="hero" class="gradient-bg text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                <div>
                    <h1 class="text-4xl md:text-6xl font-bold mb-6">Breaking Communication Barriers</h1>
                    <p class="text-xl mb-8">Our FPGA-powered AI translates sign language to speech in real-time, creating seamless communication for the deaf and hard-of-hearing community.</p>
                    <div class="flex space-x-4">
                        <button class="bg-white text-indigo-600 px-6 py-3 rounded-lg font-medium hover:bg-gray-100 transition duration-300">Try Live Demo</button>
                        <button class="border-2 border-white text-white px-6 py-3 rounded-lg font-medium hover:bg-white hover:text-indigo-600 transition duration-300">Learn More</button>
                    </div>
                </div>
                <div class="relative">
                    <div class="glass-card rounded-2xl p-6">
                        <div class="aspect-w-16 aspect-h-9 bg-gray-800 rounded-lg overflow-hidden">
                            <!-- Placeholder for video feed -->
                            <div class="w-full h-full flex items-center justify-center">
                                <i data-feather="video" class="w-16 h-16 text-gray-400"></i>
                            </div>
                        </div>
                        <div class="mt-4 flex justify-between items-center">
                            <div>
                                <h3 class="font-medium">Live Translation</h3>
                                <p class="text-sm opacity-80">FPGA processing at 120FPS</p>
                            </div>
                            <div class="flex space-x-2">
                                <button class="bg-indigo-600 p-2 rounded-full hover:bg-indigo-700">
                                    <i data-feather="mic" class="w-5 h-5"></i>
                                </button>
                                <button class="bg-indigo-600 p-2 rounded-full hover:bg-indigo-700">
                                    <i data-feather="settings" class="w-5 h-5"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div class="absolute -bottom-6 -right-6 bg-white p-4 rounded-full shadow-lg wave-animation">
                        <i data-feather="hand" class="w-10 h-10 text-indigo-600"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- How It Works Section -->
    <div class="bg-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">How Our Technology Works</h2>
                <p class="mt-4 max-w-2xl text-xl text-gray-500 mx-auto">From hand gestures to spoken words in milliseconds</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-gray-50 p-6 rounded-xl">
                    <div class="bg-indigo-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                        <i data-feather="camera" class="w-8 h-8 text-indigo-600"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-2">1. Motion Capture</h3>
                    <p class="text-gray-600">High-speed cameras capture hand and finger movements at 120 frames per second.</p>
                </div>
                <div class="bg-gray-50 p-6 rounded-xl">
                    <div class="bg-indigo-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                        <i data-feather="cpu" class="w-8 h-8 text-indigo-600"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-2">2. FPGA Processing</h3>
                    <p class="text-gray-600">Our custom FPGA hardware accelerates neural network inference for real-time analysis.</p>
                </div>
                <div class="bg-gray-50 p-6 rounded-xl">
                    <div class="bg-indigo-100 w-16 h-16 rounded-full flex items-center justify-center mb-4">
                        <i data-feather="volume-2" class="w-8 h-8 text-indigo-600"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-2">3. Speech Output</h3>
                    <p class="text-gray-600">The translated speech is generated and played through speakers or displayed as text.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Demo Section -->
    <div class="bg-gray-50 py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                <div>
                    <h2 class="text-3xl font-extrabold text-gray-900 mb-6">Try Our Real-Time Demo</h2>
                    <p class="text-gray-600 mb-8">Experience the power of our FPGA-accelerated sign language translation. Simply enable your camera and start signing to see the magic happen.</p>
                    
                    <div class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Input Source</label>
                            <select class="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
                                <option>Webcam</option>
                                <option>Video File</option>
                                <option>Sample Dataset</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Output Mode</label>
                            <select class="w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
                                <option>Speech + Text</option>
                                <option>Text Only</option>
                                <option>Speech Only</option>
                            </select>
                        </div>
                        <button class="w-full bg-indigo-600 text-white py-3 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                            Start Translation
                        </button>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-xl shadow-lg">
                    <div class="aspect-w-16 aspect-h-9 bg-gray-200 rounded-lg overflow-hidden relative">
                        <!-- Placeholder for video feed -->
                        <div class="w-full h-full flex items-center justify-center">
                            <i data-feather="video" class="w-16 h-16 text-gray-400"></i>
                        </div>
                        <div class="absolute bottom-0 left-0 right-0 bg-black bg-opacity-50 text-white p-4">
                            <div class="flex justify-between items-center">
                                <span class="font-medium">Live Feed</span>
                                <span class="text-sm">FPGA Processing: <span class="text-green-400">Active</span></span>
                            </div>
                        </div>
                    </div>
                    <div class="mt-4 bg-gray-100 p-4 rounded-lg">
                        <h4 class="font-medium text-gray-700 mb-2">Translation Output</h4>
                        <div class="bg-white p-3 rounded min-h-16">
                            <p class="text-gray-800">Sign to see translation here...</p>
                        </div>
                        <div class="mt-3 flex justify-end">
                            <button class="bg-indigo-600 text-white p-2 rounded-full hover:bg-indigo-700">
                                <i data-feather="volume-2" class="w-5 h-5"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- FPGA Advantage Section -->
    <div class="bg-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">The FPGA Advantage</h2>
                <p class="mt-4 max-w-2xl text-xl text-gray-500 mx-auto">Why our hardware-accelerated approach outperforms software-only solutions</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                <div>
                    <div class="bg-indigo-100 p-6 rounded-xl">
                        <div class="flex items-center mb-4">
                            <div class="bg-indigo-600 p-2 rounded-full mr-4">
                                <i data-feather="zap" class="w-6 h-6 text-white"></i>
                            </div>
                            <h3 class="text-xl font-bold">Lightning Fast Processing</h3>
                        </div>
                        <p class="text-gray-700">Our FPGA implementation processes sign language at 120 frames per second with less than 5ms latency, enabling truly real-time communication.</p>
                    </div>
                    
                    <div class="bg-indigo-100 p-6 rounded-xl mt-6">
                        <div class="flex items-center mb-4">
                            <div class="bg-indigo-600 p-2 rounded-full mr-4">
                                <i data-feather="battery-charging" class="w-6 h-6 text-white"></i>
                            </div>
                            <h3 class="text-xl font-bold">Low Power Consumption</h3>
                        </div>
                        <p class="text-gray-700">FPGAs provide superior performance per watt compared to GPUs, making our solution ideal for portable and battery-powered devices.</p>
                    </div>
                </div>
                
                <div>
                    <div class="bg-indigo-100 p-6 rounded-xl">
                        <div class="flex items-center mb-4">
                            <div class="bg-indigo-600 p-2 rounded-full mr-4">
                                <i data-feather="shield" class="w-6 h-6 text-white"></i>
                            </div>
                            <h3 class="text-xl font-bold">Privacy Focused</h3>
                        </div>
                        <p class="text-gray-700">All processing happens locally on the FPGA hardware - no video data is sent to the cloud, ensuring complete privacy for users.</p>
                    </div>
                    
                    <div class="bg-indigo-100 p-6 rounded-xl mt-6">
                        <div class="flex items-center mb-4">
                            <div class="bg-indigo-600 p-2 rounded-full mr-4">
                                <i data-feather="refresh-cw" class="w-6 h-6 text-white"></i>
                            </div>
                            <h3 class="text-xl font-bold">Continuous Learning</h3>
                        </div>
                        <p class="text-gray-700">Our system improves over time with user feedback, expanding its vocabulary and adapting to regional sign language variations.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Call to Action -->
    <div class="gradient-bg text-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-extrabold mb-6">Ready to Transform Communication?</h2>
            <p class="text-xl mb-8 max-w-3xl mx-auto">Join us in creating a more inclusive world where sign language is instantly understood by everyone.</p>
            <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
                <button class="bg-white text-indigo-600 px-8 py-3 rounded-lg font-medium hover:bg-gray-100 transition duration-300">Get Started</button>
                <button class="border-2 border-white text-white px-8 py-3 rounded-lg font-medium hover:bg-white hover:text-indigo-600 transition duration-300">Contact Sales</button>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                <div>
                    <div class="flex items-center">
                        <i data-feather="cpu" class="h-8 w-8 text-indigo-400"></i>
                        <span class="ml-2 text-xl font-bold">SignSpeak AI</span>
                    </div>
                    <p class="mt-4 text-gray-400">Bridging the communication gap with FPGA-powered AI.</p>
                </div>
                <div>
                    <h3 class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Product</h3>
                    <ul class="mt-4 space-y-2">
                        <li><a href="#" class="text-gray-300 hover:text-white">Features</a></li>
                        <li><a href="#" class="text-gray-300 hover:text-white">Pricing</a></li>
                        <li><a href="#" class="text-gray-300 hover:text-white">API</a></li>
                        <li><a href="#" class="text-gray-300 hover:text-white">Documentation</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Company</h3>
                    <ul class="mt-4 space-y-2">
                        <li><a href="#" class="text-gray-300 hover:text-white">About</a></li>
                        <li><a href="#" class="text-gray-300 hover:text-white">Blog</a></li>
                        <li><a href="#" class="text-gray-300 hover:text-white">Careers</a></li>
                        <li><a href="#" class="text-gray-300 hover:text-white">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-sm font-semibold text-gray-400 tracking-wider uppercase">Connect</h3>
                    <div class="mt-4 flex space-x-4">
                        <a href="#" class="text-gray-400 hover:text-white">
                            <i data-feather="twitter" class="w-5 h-5"></i>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-white">
                            <i data-feather="github" class="w-5 h-5"></i>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-white">
                            <i data-feather="linkedin" class="w-5 h-5"></i>
                        </a>
                        <a href="#" class="text-gray-400 hover:text-white">
                            <i data-feather="youtube" class="w-5 h-5"></i>
                        </a>
                    </div>
                    <div class="mt-4">
                        <p class="text-gray-400">Subscribe to our newsletter</p>
                        <div class="mt-2 flex">
                            <input type="email" placeholder="Your email" class="px-3 py-2 rounded-l text-gray-900 w-full">
                            <button class="bg-indigo-600 px-4 py-2 rounded-r">
                                <i data-feather="send" class="w-5 h-5"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="mt-12 border-t border-gray-800 pt-8">
                <p class="text-gray-400 text-sm text-center">&copy; 2023 SignSpeak AI. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        feather.replace();
        
        // Initialize Vanta.js globe effect
        VANTA.GLOBE({
            el: "#hero",
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x6366f1,
            backgroundColor: 0x8b5cf6,
            size: 1.00
        });
        
        // Mobile menu toggle functionality would go here
        document.querySelector('[aria-controls="mobile-menu"]').addEventListener('click', function() {
            // Toggle mobile menu
        });
        
        // Demo functionality would connect to your FPGA backend
        document.querySelector('#start-translation').addEventListener('click', function() {
            // Connect to camera and FPGA processing
            // Display real-time translation
        });
    </script>
</body>
</html>


To make this project come to life, here's a step-by-step implementation guide:

1. **Hardware Setup**:
   - Connect your FPGA board to a camera module (USB or dedicated camera interface)
   - Ensure the FPGA is connected to your server/computer via USB or Ethernet

2. **Backend Integration**:
   - Create a Node.js/Flask server to handle communication between the web interface and FPGA
   - Implement WebSocket connections for real-time data transfer
   - Create API endpoints for:
     - Starting/stopping the camera feed
     - Receiving processed translation data from FPGA
     - Controlling output modes (speech/text)

3. **Frontend Implementation**:
   - The HTML/CSS/JS provided above gives you a complete UI
   - Add JavaScript to:
     - Access the user's webcam via `navigator.mediaDevices.getUserMedia()`
     - Stream video to your backend for FPGA processing
     - Display real-time translation results
     - Implement text-to-speech using the Web Speech API

4. **FPGA Communication**:
   - Modify your existing FPGA code to:
     - Accept video frames from the web interface
     - Return processed results (sign language to text mappings)
     - Handle different output modes

5. **Deployment**:
   - Host the frontend on Vercel/Netlify
   - Deploy the backend on a cloud service with FPGA access (AWS EC2 F1, etc.)
   - For local testing, use ngrok to expose your local server

Key files to create:
- `server.js` - Backend server handling FPGA communication
- `public/js/app.js` - Frontend logic for camera and translation UI
- `public/css/styles.css` - Additional custom styles
- `api/` - Folder containing FPGA communication APIs

The provided UI already includes:
- Real-time video display area
- Translation output display
- Controls for input/output modes
- FPGA status indicators
- Responsive design for all devices

To connect to your GitHub project:
1. Clone your existing repo
2. Add this UI code in a new `web-ui` folder
3. Create the backend integration files
4. Update your FPGA code to work with the web interface
5. Test locally before deploying

Would you like me to provide the specific backend integration code or any particular part in more detail?