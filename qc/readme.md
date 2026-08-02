<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>MacBook Pro Field Inspection</title>
  <style>
    :root {
      --bg: #0f172a;
      --card-bg: #1e293b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-success: #22c55e;
      --accent-danger: #ef4444;
      --accent-warning: #f59e0b;
      --border: #334155;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      padding-bottom: 80px;
    }

    /* Sticky Header & Progress Bar */
    header {
      position: sticky;
      top: 0;
      background-color: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 16px;
      z-index: 100;
    }

    .header-content {
      max-width: 600px;
      margin: 0 auto;
    }

    .title-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }

    h1 {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text);
    }

    .progress-text {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--accent);
    }

    .progress-bar-bg {
      width: 100%;
      height: 8px;
      background-color: var(--border);
      border-radius: 4px;
      overflow: hidden;
    }

    .progress-bar-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--accent), var(--accent-success));
      transition: width 0.3s ease;
    }

    /* Main Content Layout */
    main {
      max-width: 600px;
      margin: 0 auto;
      padding: 16px;
    }

    /* Target Banner */
    .target-card {
      background-color: var(--card-bg);
      border: 1px solid var(--accent);
      border-radius: 12px;
      padding: 14px;
      margin-bottom: 20px;
    }

    .target-card h2 {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent);
      margin-bottom: 4px;
    }

    .target-card p {
      font-size: 0.95rem;
      font-weight: 600;
    }

    /* Rules Banner */
    .rule-card {
      background-color: rgba(239, 68, 68, 0.1);
      border-left: 4px solid var(--accent-danger);
      padding: 12px;
      border-radius: 4px 8px 8px 4px;
      margin-bottom: 24px;
      font-size: 0.85rem;
      font-weight: 600;
      color: #fca5a5;
    }

    /* Section Styling */
    section {
      margin-bottom: 28px;
    }

    .section-header {
      font-size: 1rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* To-do Item Cards */
    .todo-item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      background-color: var(--card-bg);
      border: 1px solid var(--border);
      padding: 14px;
      border-radius: 10px;
      margin-bottom: 8px;
      cursor: pointer;
      user-select: none;
      transition: transform 0.1s ease, border-color 0.2s ease, background-color 0.2s ease;
    }

    .todo-item:active {
      transform: scale(0.98);
    }

    /* Checkbox Styling */
    .checkbox {
      width: 22px;
      height: 22px;
      border-radius: 6px;
      border: 2px solid var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
      transition: all 0.2s ease;
    }

    .checkbox svg {
      width: 14px;
      height: 14px;
      fill: none;
      stroke: white;
      stroke-width: 3;
      stroke-linecap: round;
      stroke-linejoin: round;
      opacity: 0;
      transform: scale(0.5);
      transition: all 0.2s ease;
    }

    .todo-content {
      flex: 1;
    }

    .todo-text {
      font-size: 0.95rem;
      color: var(--text);
      line-height: 1.35;
    }

    .code-block {
      background-color: #090d16;
      border: 1px solid var(--border);
      color: #e2e8f0;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.8rem;
      padding: 8px 10px;
      border-radius: 6px;
      margin-top: 8px;
      word-break: break-all;
      user-select: all;
    }

    /* Checked State */
    .todo-item.checked {
      border-color: rgba(34, 197, 94, 0.3);
      background-color: rgba(30, 41, 59, 0.5);
    }

    .todo-item.checked .checkbox {
      background-color: var(--accent-success);
      border-color: var(--accent-success);
    }

    .todo-item.checked .checkbox svg {
      opacity: 1;
      transform: scale(1);
    }

    .todo-item.checked .todo-text {
      text-decoration: line-through;
      color: var(--text-muted);
    }

    /* Callout Boxes inside lists */
    .callout {
      padding: 10px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      margin-top: 8px;
      line-height: 1.3;
    }

    .callout-danger {
      background-color: rgba(239, 68, 68, 0.15);
      border: 1px solid var(--accent-danger);
      color: #fca5a5;
    }

    .callout-warning {
      background-color: rgba(245, 158, 11, 0.15);
      border: 1px solid var(--accent-warning);
      color: #fde68a;
    }

    /* Fixed Reset Button at Bottom */
    .reset-btn {
      position: fixed;
      bottom: 16px;
      right: 16px;
      background-color: var(--border);
      color: var(--text);
      border: none;
      padding: 10px 16px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(0,0,0,0.5);
      cursor: pointer;
      z-index: 99;
    }

    .reset-btn:active {
      transform: scale(0.95);
    }
  </style>
</head>
<body>

  <header>
    <div class="header-content">
      <div class="title-row">
        <h1>MacBook Field Inspection</h1>
        <div class="progress-text" id="progressText">0% Complete</div>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" id="progressBar"></div>
      </div>
    </div>
  </header>

  <main>
    <div class="target-card">
      <h2>Target Specs</h2>
      <p>16-inch M1 Max | 64GB Memory | 1TB SSD</p>
    </div>

    <div class="rule-card">
      ⚠️ RULE: Do not transfer money until all mandatory checks pass.
    </div>

    <!-- PHASE 0 -->
    <section>
      <div class="section-header">Phase 0: Pre-Arrival Preparation</div>
      
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Bring USB-C / Thunderbolt external drive</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Bring USB-C cables, SD card, and headphones</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Bring phone with active hotspot enabled</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Have your Apple ID credentials ready</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Ask seller for original invoice/box/serial details</div></div>
      </label>
    </section>

    <!-- PHASE 1 -->
    <section>
      <div class="section-header">Phase 1: Physical Triage</div>

      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Inspect 4 corners & known dent (confirm strictly cosmetic)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Check chassis for bends, twisting, or uneven gaps</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Inspect bottom case & screws for screwdriver/tamper marks</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Inspect glass/frame for cracks or pressure spots</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Test hinge action (~10 opens/closes, sits flush when shut)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Inspect inside of every port for physical damage</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content">
          <div class="todo-text">Ask seller direct history: repair marks, liquid damage, board/display/battery replacements?</div>
        </div>
      </label>
    </section>

    <!-- PHASE 2 -->
    <section>
      <div class="section-header">Phase 2: Power-On & Specs</div>

      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content">
          <div class="todo-text">Check <b> → About This Mac</b></div>
          <div class="callout callout-warning">Must show: M1 Max / 64GB / 1TB</div>
        </div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content">
          <div class="todo-text">Verify Serial in Terminal vs. Box vs. About This Mac</div>
          <div class="code-block">system_profiler SPHardwareDataType</div>
        </div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content">
          <div class="todo-text">Verify MDM / Corporate Enrollment Status</div>
          <div class="code-block">profiles status -type enrollment</div>
          <div class="code-block">sudo profiles show -type enrollment</div>
          <div class="callout callout-danger">Must show: Enrolled via DEP: No | MDM enrollment: No</div>
        </div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content">
          <div class="todo-text">Check <b>System Settings → General → Device Management</b> (Ensure empty)</div>
        </div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content">
          <div class="todo-text">Check Battery Health (Target: ~106 cycles / ~94% capacity)</div>
          <div class="callout callout-warning">System Settings → Battery → Health must be "Normal"</div>
        </div>
      </label>
    </section>

    <!-- PHASE 3 -->
    <section>
      <div class="section-header">Phase 3: Hardware & Ports Test</div>

      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">MagSafe charging (LED turns on, percentage increases)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Test read/write on <b>ALL USB-C / Thunderbolt Ports</b></div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Test SD Card slot (Read/Write)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Test HDMI port out to external screen/audio</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Headphone jack (L/R channels, no crackling)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Keyboard test (Type EVERY key in TextEdit + TouchID)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Trackpad test (Click full surface, gestures, force touch)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Display test (Check solid colors for dead pixels/bright spots)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Camera, Microphone (Photo Booth check) & Speakers</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Connect Wi-Fi (Hotspot test) & pair Bluetooth device</div></div>
      </label>
    </section>

    <!-- PHASE 4 -->
    <section>
      <div class="section-header">Phase 4: Diagnostics & Stress Tests</div>

      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content">
          <div class="todo-text">Run Apple Diagnostics</div>
          <div class="callout">Shutdown → Hold Power → Startup Options → Press <b>Cmd + D</b></div>
        </div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Blackmagic Disk Speed Test (Multi-GB/s read/write required)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Run Cinebench / Geekbench (No crashes, artifacts, or throttling)</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Run Dev Workflow (Cursor, Next.js build, Docker, local Ollama/MLX model)</div></div>
      </label>
    </section>

    <!-- PHASE 5 -->
    <section>
      <div class="section-header">Phase 5: The Ultimate Gatekeeper (Reset Pass)</div>

      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content"><div class="todo-text">Seller signs out of Apple Account / Find My</div></div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content">
          <div class="todo-text">Execute: <b>Erase All Content and Settings</b></div>
        </div>
      </label>
      <label class="todo-item">
        <div class="checkbox"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
        <div class="todo-content">
          <div class="todo-text">Complete Setup Assistant via Hotspot</div>
          <div class="callout callout-danger">WALK AWAY IMMEDIATELY IF: Activation Lock or Remote Management appears.</div>
        </div>
      </label>
    </section>

  </main>

  <button class="reset-btn" onclick="resetAll()">Reset Checklist</button>

  <script>
    const items = document.querySelectorAll('.todo-item');
    const progressBar = document.getElementById('progressBar');
    const progressText = document.getElementById('progressText');

    // Load state
    function loadState() {
      const saved = JSON.parse(localStorage.getItem('macbook_checklist_state') || '{}');
      items.forEach((item, index) => {
        if (saved[index]) {
          item.classList.add('checked');
        } else {
          item.classList.remove('checked');
        }
      });
      updateProgress();
    }

    // Save state
    function saveState() {
      const state = {};
      items.forEach((item, index) => {
        state[index] = item.classList.contains('checked');
      });
      localStorage.setItem('macbook_checklist_state', JSON.stringify(state));
    }

    // Update Progress Bar
    function updateProgress() {
      const total = items.length;
      const checkedCount = document.querySelectorAll('.todo-item.checked').length;
      const percentage = Math.round((checkedCount / total) * 100);

      progressBar.style.width = percentage + '%';
      progressText.textContent = `${percentage}% Complete`;
    }

    // Toggle items
    items.forEach((item) => {
      item.addEventListener('click', (e) => {
        // Prevent click trigger if clicking inside code blocks to select text
        if (e.target.classList.contains('code-block')) return;
        
        item.classList.toggle('checked');
        saveState();
        updateProgress();
      });
    });

    // Reset All Function
    function resetAll() {
      if (confirm("Reset all checkboxes?")) {
        localStorage.removeItem('macbook_checklist_state');
        loadState();
      }
    }

    // Initialize
    loadState();
  </script>
</body>
</html>
