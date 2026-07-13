document.addEventListener('DOMContentLoaded', function() {
    // --- 1. 产品分类切换逻辑 (修复点击无效问题) ---
    const categoryContainers = document.querySelectorAll('.material-section');
    
    categoryContainers.forEach(container => {
        const tabs = container.querySelectorAll('.category-tab');
        const cards = container.querySelectorAll('.product-card');

        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const category = tab.getAttribute('data-category');

                // 更新按钮激活状态
                tabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');

                // 执行分类过滤
                cards.forEach(card => {
                    const cardCategory = card.getAttribute('data-category');
                    if (category === 'all' || cardCategory === category) {
                        card.style.display = 'block';
                        card.style.opacity = '0';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transition = 'opacity 0.4s ease';
                        }, 10);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    });

    // --- 2. 统一处理全站所有询盘表单 (首页底部和独立页) ---
    // --- 2. Handle inquiry forms with one FormSubmit request ---
    document.querySelectorAll('.inquiry-form:not([data-native-submit="true"])').forEach(form => {
        form.addEventListener('submit', function(e) {
            if (this.dataset.nativeSubmit === 'true') {
                return;
            }

            if (this.dataset.submitting === 'true') {
                e.preventDefault();
                return;
            }
            this.dataset.submitting = 'true';

            const submitButton = this.querySelector('[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.textContent = 'Sending...';
            }

            // 找感谢 div：优先用 data-thankyou-target，否则找同级 .thank-you-inline
            const targetId = this.getAttribute('data-thankyou-target');
            const thankYouDiv = targetId
                ? document.getElementById(targetId)
                : this.parentElement.querySelector('.thank-you-inline');

            // 用 FormData 直接从表单构建，确保附件包含在内
            form.style.setProperty('display', 'none', 'important');
            if (thankYouDiv) {
                const displayMode = targetId ? 'flex' : 'block';
                thankYouDiv.style.setProperty('display', displayMode, 'important');
                thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }

            if (typeof gtag !== 'undefined') {
                gtag('event', 'form_submission_web', {
                    'event_category': 'Inquiry',
                    'event_label': 'FormSubmit'
                });
            }

            if (this.dataset.nativeSubmit === 'true') {
                return;
            }

            e.preventDefault();
            const formData = new FormData(this);

            fetch('https://formsubmit.co/ajax/sales@aizjewelry.com', {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' }
            }).then(function() {
                // 成功后显示感谢界面
                form.style.setProperty('display', 'none', 'important');
                form.style.setProperty('display', 'none', 'important');
                if (thankYouDiv) {
                    thankYouDiv.style.setProperty('display', 'flex', 'important');
                    thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'form_submission_web', {
                        'event_category': 'Inquiry',
                        'event_label': 'FormSubmit'
                    });
                }
            }).catch(function() {
                // 失败时恢复按钮
                form.dataset.submitting = 'false';
                if (submitButton) {
                    submitButton.disabled = false;
                    submitButton.textContent = 'Inquire Now';
                }
                alert('Something went wrong. Please try again or email us directly at sales@aizjewelry.com');
            });
        });
    });

    // Legacy handler disabled after the footer form moved to the single-send handler above.
    document.querySelectorAll('.inquiry-form-legacy-disabled').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const formContainer = this.parentElement;
            const thankYouDiv = formContainer.querySelector('.thank-you-inline');

            // 瞬间视觉反馈
            this.style.setProperty('display', 'none', 'important');
            if (thankYouDiv) {
                thankYouDiv.style.setProperty('display', 'block', 'important');
                thankYouDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }

            // 后台异步发送
            const formData = new FormData(this);
        });
    });

    // --- 3. 语言切换器逻辑 ---
    document.querySelectorAll('.lang-switcher').forEach(switcher => {
        switcher.addEventListener('click', function(e) {
            if (window.innerWidth <= 992) {
                e.stopPropagation();
                this.classList.toggle('active');
            }
        });
    });
    document.addEventListener('click', function() {
        document.querySelectorAll('.lang-switcher').forEach(s => s.classList.remove('active'));
    });

    // --- 4. Shared upload zones for inquiry forms ---
    initUploadZones();
});

function initUploadZones() {
    const zones = Array.from(document.querySelectorAll('.upload-zone'));
    if (!zones.length) return;

    let activeZone = zones[0];

    function renderZone(zone) {
        const fileInput = zone.querySelector('.file-input');
        const fileList = zone.querySelector('.file-list');
        const multiNote = zone.querySelector('.multi-file-note');
        const state = zone._uploadState || { files: [] };
        zone._uploadState = state;

        if (fileList) {
            fileList.innerHTML = '';
            state.files.forEach(function(file, index) {
                const item = document.createElement('div');
                item.className = 'file-item';

                const label = document.createElement('span');
                label.className = 'file-item-label';
                label.textContent = file.name;

                const meta = document.createElement('span');
                meta.className = 'file-item-meta';
                meta.textContent = '(' + (file.size / 1024).toFixed(1) + ' KB)';

                const textWrap = document.createElement('span');
                textWrap.className = 'file-item-text';
                textWrap.appendChild(document.createTextNode('File: '));
                textWrap.appendChild(label);
                textWrap.appendChild(document.createTextNode(' '));
                textWrap.appendChild(meta);

                const removeBtn = document.createElement('button');
                removeBtn.type = 'button';
                removeBtn.className = 'remove-btn';
                removeBtn.setAttribute('aria-label', 'Remove file');
                removeBtn.dataset.idx = String(index);
                removeBtn.textContent = 'x';

                item.appendChild(textWrap);
                item.appendChild(removeBtn);
                fileList.appendChild(item);
            });
        }

        if (fileInput) {
            if (state.files.length > 0) {
                const dt = new DataTransfer();
                dt.items.add(state.files[0]);
                fileInput.files = dt.files;
            } else {
                fileInput.value = '';
            }
        }

        if (multiNote) {
            multiNote.style.display = state.files.length > 1 ? 'block' : 'none';
        }

        zone.classList.toggle('has-files', state.files.length > 0);
    }

    function addFiles(zone, incomingFiles) {
        const state = zone._uploadState || { files: [] };
        const nextFiles = Array.from(incomingFiles || []).filter(Boolean);
        if (!nextFiles.length) return;
        state.files = state.files.concat(nextFiles);
        zone._uploadState = state;
        renderZone(zone);
    }

    function getPasteFiles(event) {
        const clipboard = event.clipboardData;
        if (!clipboard || !clipboard.items) return [];
        return Array.from(clipboard.items)
            .filter(function(item) { return item.kind === 'file'; })
            .map(function(item) { return item.getAsFile(); })
            .filter(Boolean);
    }

    zones.forEach(function(zone) {
        const fileInput = zone.querySelector('.file-input');
        const fileList = zone.querySelector('.file-list');

        zone.tabIndex = 0;
        zone.setAttribute('role', 'button');
        zone.setAttribute('aria-label', 'Upload attachments');

        zone.addEventListener('click', function(event) {
            if (event.target.closest('.remove-btn')) return;
            if (event.target.closest('.file-list')) return;
            activeZone = zone;
            zone.focus();
            if (fileInput) fileInput.click();
        });

        zone.addEventListener('focusin', function() {
            activeZone = zone;
        });

        if (fileInput) {
            fileInput.addEventListener('change', function() {
                addFiles(zone, fileInput.files);
            });
        }

        zone.addEventListener('dragover', function(event) {
            event.preventDefault();
            zone.classList.add('drag-over');
            activeZone = zone;
        });

        zone.addEventListener('dragleave', function() {
            zone.classList.remove('drag-over');
        });

        zone.addEventListener('drop', function(event) {
            event.preventDefault();
            zone.classList.remove('drag-over');
            activeZone = zone;
            addFiles(zone, event.dataTransfer && event.dataTransfer.files);
        });

        if (fileList) {
            fileList.addEventListener('click', function(event) {
                const button = event.target.closest('.remove-btn');
                if (!button) return;
                const state = zone._uploadState || { files: [] };
                const index = Number(button.dataset.idx);
                if (Number.isNaN(index)) return;
                state.files.splice(index, 1);
                zone._uploadState = state;
                renderZone(zone);
            });
        }

        renderZone(zone);
    });

    document.addEventListener('paste', function(event) {
        const files = getPasteFiles(event);
        if (!files.length) return;
        const focusedZone = activeZone && activeZone.contains(document.activeElement) ? activeZone : null;
        const zone = focusedZone || (document.activeElement && document.activeElement.closest ? document.activeElement.closest('.upload-zone') : null);
        if (!zone) return;
        addFiles(zone, files);
    });
}

// --- 4. 文件上传显示辅助函数 ---
function updateFileName(input) {
    const fileName = input.files.length > 0 ? input.files[0].name : "";
    const display = input.parentElement.querySelector('.file-name-display');
    if (display && fileName) { display.textContent = fileName; }
}
