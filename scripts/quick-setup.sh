#!/bin/bash

# Note: Not using 'set -e' to allow script to handle errors gracefully

# Test mode flag - set to 1 to simulate without executing
TEST_MODE=${TEST_MODE:-0}

if [ "$TEST_MODE" = "1" ]; then
    echo "========================================="
    echo "TEST MODE - No changes will be made"
    echo "========================================="
    echo ""
fi

echo "========================================="
echo "Claude Code for Product Managers Course"
echo "Quick Setup Script"
echo "========================================="
echo ""

# Check Node.js version
echo "Checking prerequisites..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version | cut -d 'v' -f 2 | cut -d '.' -f 1)
    if [ "$NODE_VERSION" -ge 18 ]; then
        echo "✓ Node.js $(node --version) installed"
    else
        echo "⚠️  Node.js $(node --version) found, but version 18+ required"
        echo "Upgrading Node.js..."
        if [ "$TEST_MODE" = "1" ]; then
            echo "[TEST] Would upgrade Node.js via Homebrew"
        else
            brew upgrade node
        fi
    fi
else
    echo "Node.js not found. Installing..."
    if [ "$TEST_MODE" = "1" ]; then
        echo "[TEST] Would install Node.js"
    else
        # Check if Homebrew is installed
        if ! command -v brew &> /dev/null; then
            echo "Installing Homebrew first..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" < /dev/null
        fi

        echo "Installing Node.js via Homebrew..."
        brew install node < /dev/null

        # Add Homebrew's bin directory to PATH for this script session
        export PATH="/opt/homebrew/bin:$PATH"

        echo "✓ Node.js installed"
    fi
fi

echo ""

# Check if Claude Code is already installed
if command -v claude &> /dev/null; then
    echo "✓ Claude Code is already installed"
else
    echo "Installing Claude Code..."
    if [ "$TEST_MODE" = "1" ]; then
        echo "[TEST] Would run: curl -fsSL https://claude.ai/install.sh | bash"
        echo "✓ [TEST] Claude Code installation simulated"
    else
        curl -fsSL https://claude.ai/install.sh | bash < /dev/null

        # Try to add to PATH for this session
        # Claude Code typically installs to ~/.local/bin on macOS/Linux
        export PATH="$HOME/.local/bin:$PATH"

        # Verify installation
        if command -v claude &> /dev/null; then
            echo "✓ Claude Code installed successfully"
        else
            echo ""
            echo "⚠️  Claude Code installed, but not available in current session."
            echo "   Please restart your terminal and run this script again:"
            echo ""
            echo "   curl -fsSL https://raw.githubusercontent.com/yuezheng2006/claude-code-pm-course/main/scripts/quick-setup.sh | bash"
            echo ""
            exit 1
        fi
    fi
fi

echo ""
echo "Downloading course materials..."

# Course materials will extract to Documents/claude-code-course/
COURSE_DIR="$HOME/Documents/claude-code-course"

if [ "$TEST_MODE" = "1" ]; then
    echo "[TEST] Would download course to: $HOME/Documents/course.zip"
    echo "[TEST] Would extract to: $COURSE_DIR"
    echo "✓ [TEST] Course materials download simulated"
else
    # Ensure Documents directory exists
    if [ ! -d "$HOME/Documents" ]; then
        mkdir -p "$HOME/Documents"
    fi

    cd "$HOME/Documents" || {
        echo "❌ Failed to navigate to Documents directory"
        exit 1
    }

    # Remove existing course materials if they exist
    if [ -d "$COURSE_DIR" ]; then
        echo "Found existing course materials. Removing..."
        rm -rf "$COURSE_DIR"
    fi

    # Download and extract course materials into claude-code-course folder
    echo "Downloading course zip..."
    if ! curl -L https://github.com/yuezheng2006/claude-code-pm-course/releases/latest/download/complete-course.zip -o course.zip; then
        echo "❌ Failed to download course materials"
        exit 1
    fi

    echo "Extracting course materials..."
    if ! unzip -q course.zip -d claude-code-course; then
        echo "❌ Failed to extract course materials"
        rm -f course.zip
        exit 1
    fi
    rm course.zip

    # Verify extraction was successful
    if [ ! -d "$COURSE_DIR/.claude" ]; then
        echo "❌ Course materials extraction failed - .claude directory not found"
        exit 1
    fi

    echo "✓ Course materials extracted to: $COURSE_DIR"
fi
echo ""
echo "========================================="
echo "Setup Complete!"
echo "========================================="
echo ""
echo "Starting the course..."
echo ""

if [ "$TEST_MODE" = "1" ]; then
    echo "[TEST] Would navigate to: $COURSE_DIR"
    echo "[TEST] Would run: claude \"/start-1-1\""
    echo ""
    echo "========================================="
    echo "TEST COMPLETE - No changes were made"
    echo "========================================="
else
    # Navigate to course directory and launch Claude Code
    # Redirect stdin from /dev/tty to enable interactive mode when piped
    if [ ! -d "$COURSE_DIR" ]; then
        echo "❌ Course directory not found: $COURSE_DIR"
        exit 1
    fi

    cd "$COURSE_DIR" || {
        echo "❌ Failed to navigate to course directory: $COURSE_DIR"
        exit 1
    }

    # Verify we're in the right directory
    if [ ! -d ".claude" ]; then
        echo "❌ Error: .claude directory not found. Please ensure you're in the course-materials directory."
        exit 1
    fi

    echo "Launching Claude Code..."
    claude "/start-1-1" < /dev/tty
fi
