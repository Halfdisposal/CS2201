" ==============================================================================
"  .vimrc
" ------------------------------------------------------------------------------
"  A powerful and well-structured Vim configuration file.
"  This file is for Vim version 9.1 on a Linux system.
"  It uses vim-plug for plugin management.
"
"  File Structure:
"  ~/.vimrc
"  ~/.vim/
"      - plugin/
"      - autoload/
"      - colors/
"
"  Installation:
"  1. Paste this content into your ~/.vimrc file.
"  2. Open Vim and type :PlugInstall to install all the plugins.
"  ==============================================================================


" ==============================================================================
"  1. General Settings
" ------------------------------------------------------------------------------
"  These are basic settings for a better user experience.
"  ------------------------------------------------------------------------------

set nocompatible              " Be iMproved, required
set autoindent                " Enable automatic indentation
set expandtab                 " Use spaces instead of tabs
set tabstop=4                 " Number of spaces a <Tab> in the file counts for
set shiftwidth=4              " Number of spaces to indent
set softtabstop=4             " Number of spaces to use when pressing <Tab>
set number                    " Show line numbers
set number                    " Show line numbers
set cursorline                " Highlight the current line
set smartcase                 " Smart case search
set ignorecase                " Ignore case when searching
set mouse=a                   " Enable mouse support in all modes
set showmode                  " Show current mode
set showcmd                   " Show incomplete commands
set hidden                    " Hide buffers when they are abandoned
set wrap                    " Wrap lines
set scrolloff=8               " Lines of context when scrolling
set updatetime=300            " Time in ms for when vim writes a swap file to disk
set wildmenu                  " Enable enhanced command-line completion
set fileformat=unix           " Use Unix file format
set backspace=indent,eol,start " Make backspace work as you'd expect


" ==============================================================================
"  2. Vim-Plug
" ------------------------------------------------------------------------------
"  The simplest Vim plugin manager.
"  Install with: curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
"      https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
" ------------------------------------------------------------------------------

call plug#begin('~/.vim/plugged')

" Plugins Section - Add your plugins here
Plug 'junegunn/vim-plug'
Plug 'sainnhe/everforest'           " A nice dark colorscheme
Plug 'vim-airline/vim-airline'     " A lean & mean status/tabline for Vim
Plug 'vim-airline/vim-airline-themes' " Themes for airline
Plug 'preservim/nerdtree'          " A tree explorer for Vim
Plug 'tpope/vim-surround'          " A plugin for surrounding text
Plug 'tpope/vim-commentary'        " A plugin for commenting out code


Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'tomasr/molokai'
Plug 'joshdick/onedark.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'morhetz/gruvbox'
Plug 'ayu-theme/ayu-vim'
Plug 'folke/tokyonight.nvim'
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'sainnhe/sonokai'
Plug 'sainnhe/edge'
Plug 'rakr/vim-one'
Plug 'altercation/vim-colors-solarized'
Plug 'NLKNguyen/papercolor-theme'
Plug 'lifepillar/vim-solarized8'

call plug#end()


" ============================================================================
" COLORSCHEME SETTINGS
" ============================================================================
set termguicolors             " Enable true color support
set background=dark           " Dark background

" Everforest configuration
let g:everforest_background = 'hard'
let g:everforest_better_performance = 1
let g:everforest_enable_italic = 1
let g:everforest_disable_italic_comment = 0

" Gruvbox configuration
let g:gruvbox_contrast_dark = 'hard'
let g:gruvbox_improved_strings = 1
let g:gruvbox_improved_warnings = 1

" OneDark configuration
let g:onedark_termcolors = 256
let g:onedark_terminal_italics = 1

" Ayu configuration
let ayucolor = "dark"  " for dark version of theme

" Sonokai configuration
let g:sonokai_style = 'default'
let g:sonokai_enable_italic = 1
let g:sonokai_disable_italic_comment = 0

" Edge configuration
let g:edge_style = 'default'
let g:edge_enable_italic = 1
let g:edge_disable_italic_comment = 0

" One configuration
let g:one_allow_italics = 1

" Solarized configuration
let g:solarized_termcolors = 256
let g:solarized_termtrans = 1

" PaperColor configuration
let g:PaperColor_Theme_Options = {
  \   'theme': {
  \     'default': {
  \       'transparent_background': 0
  \     }
  \   }
  \ }

" Set the colorscheme (change this to switch themes)
colorscheme edge

" ============================================================================
" COLORSCHEME SWITCHING FUNCTIONS
" ============================================================================

" Function to switch color schemes easily
function! SwitchColorScheme(scheme)
    try
        execute 'colorscheme ' . a:scheme
        echo 'Switched to colorscheme: ' . a:scheme
    catch
        echo 'Colorscheme ' . a:scheme . ' not found!'
    endtry
endfunction

" Commands to switch color schemes quickly
command! Everforest call SwitchColorScheme('everforest')
command! Dracula call SwitchColorScheme('dracula')
command! Molokai call SwitchColorScheme('molokai')
command! OneDark call SwitchColorScheme('onedark')
command! Nord call SwitchColorScheme('nord')
command! Gruvbox call SwitchColorScheme('gruvbox')
command! Ayu call SwitchColorScheme('ayu')
command! Sonokai call SwitchColorScheme('sonokai')
command! Edge call SwitchColorScheme('edge')
command! One call SwitchColorScheme('one')
command! Solarized call SwitchColorScheme('solarized')
command! Solarized8 call SwitchColorScheme('solarized8')
command! PaperColor call SwitchColorScheme('PaperColor')
command! Catppuccin call SwitchColorScheme('catppuccin_frappe')

" Function to cycle through favorite color schemes
let g:color_schemes = ['everforest', 'dracula', 'gruvbox', 'onedark', 'nord', 'molokai', 'ayu']
let g:current_scheme_index = 0

function! CycleColorScheme()
    let g:current_scheme_index = (g:current_scheme_index + 1) % len(g:color_schemes)
    let l:scheme = g:color_schemes[g:current_scheme_index]
    call SwitchColorScheme(l:scheme)
endfunction

" List all available color schemes
function! ListColorSchemes()
    echo "Available color schemes:"
    for scheme in g:color_schemes
        echo "  " . scheme
    endfor
    echo "\nUse :Colorscheme<Name> to switch (e.g., :Dracula)"
    echo "Use <leader>cc to cycle through schemes"
    echo "Use :ListColors to see this list again"
endfunction

command! ListColors call ListColorSchemes()



" ==============================================================================
"  4. Statusline (vim-airline)
" ------------------------------------------------------------------------------
"  This configures the statusline to show:
"  - Left: Mode, filename, git branch
"  - Right: Time, filetype, character encoding
"  ------------------------------------------------------------------------------

let g:airline_powerline_fonts = 1
let g:airline_theme = 'everforest'


let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'

" Custom statusline sections to match the request
" Left side: Mode, filename
let g:airline_section_a = airline#section#create(['mode'])
let g:airline_section_b = airline#section#create(['file'])

" Right side: Time, filetype, character encoding
let g:airline_section_c = '%{getcwd()}'
let g:airline_section_x = '%{&filetype}'
let g:airline_section_y = 'Reg:%{v:register} Buf:%n'
let g:airline_section_z = '%{strftime("%H:%M")} %p%% %l:%c'


" ==============================================================================
"  5. Mappings
" ------------------------------------------------------------------------------
"  Custom key mappings for a smoother workflow.
"  ------------------------------------------------------------------------------
let &t_SI = "\e[6 q"          " Bar cursor in insert mode
let &t_EI = "\e[2 q"          " Block cursor in normal mode
let &t_SR = "\e[4 q"          " Underline cursor in replace mode


let mapleader = "\<Space>"
let maplocalleader = ","

" NERDTree mappings
nnoremap <leader>n :NERDTreeToggle<CR>
nnoremap <leader>f :NERDTreeFind<CR>


let g:NERDTreeWinSize = 30
let g:NERDTreeShowHidden = 1
let g:NERDTreeQuitOnOpen = 0
let g:NERDTreeAutoDeleteBuffer = 1
let g:NERDTreeMinimalUI = 1

" Fast saving and quitting
nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <leader>wq :wq<CR>
nnoremap <leader>qq :qa!<CR>

" Better window navigation
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l





" ============================================================================
" AUTOCOMMANDS
" ============================================================================
augroup vimrc_autocmds
    autocmd!
    
    " Remove trailing whitespace on save
    autocmd BufWritePre * :%s/\s\+$//e
    
    " Auto-reload .vimrc when saved
    autocmd BufWritePost .vimrc source %
    
    " Highlight TODO, FIXME, etc.
    autocmd WinEnter,VimEnter * :silent! call matchadd('Todo', 'TODO\|FIXME\|NOTE\|BUG\|HACK', -1)
    
    " File type specific settings
    autocmd FileType python setlocal tabstop=4 shiftwidth=4 softtabstop=4
    autocmd FileType javascript setlocal tabstop=2 shiftwidth=2 softtabstop=2
    autocmd FileType html setlocal tabstop=2 shiftwidth=2 softtabstop=2
    autocmd FileType css setlocal tabstop=2 shiftwidth=2 softtabstop=2
    autocmd FileType vim setlocal tabstop=2 shiftwidth=2 softtabstop=2
    
augroup END
