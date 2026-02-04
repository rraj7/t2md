# Reusable Prompt: Transcripts to Markdown

## The Prompt


    This directory contains video transcripts for my [COURSE NAME] course, specifically [MODULE/UNIT NAME].  
      
    Please create a new Markdown document that formats the content into readable prose with mild edits so I can read it more like a textbook.  
      
    Key requirements:  
    1. The documents were downloaded in the order they should be watched - earlier timestamps or file modification dates indicate that document should appear earlier in the combined document  
    2. Transform conversational transcript language into polished textbook-style prose  
    3. Organize content logically with clear chapter/section headings based on themes  
    4. Preserve ALL important examples, case studies, and key concepts  
    5. Remove transcript artifacts (line numbers, timestamps, filler words)  
    6. Create smooth transitions between topics  
    7. Include a table of contents or clear hierarchical structure  
    8. Add a summary section at the end that ties key concepts together  
    9. Name the output file: [MODULE_NAME]_Reading.md  
      
    Please read all transcript files first to understand the full scope, then create the combined document.

* * *

## Optimization Tips for the AI

### Pre-Processing Checklist

- List all files with timestamps to determine correct order
- Identify the numbering/naming convention in filenames (e.g., 3.7.1, 3.7.2, 3.9.1, 3.10.1)
- Read all files in parallel for efficiency
- Analyze content themes before organizing into chapters

### Transformation Guidelines

**Remove:**

- Line numbers from transcripts
- Timestamp markers
- Filler words (um, uh, you know)
- Repetitive phrasing from spoken delivery
- Awkward sentence breaks from speech patterns

**Preserve:**

- All examples with full context
- Real-world scenarios and case studies
- Key one-liners and memorable phrases
- Important definitions and frameworks
- Names of scholars/authors referenced
- Specific recommendations and action items

**Enhance:**

- Create logical chapter/section breaks
- Add descriptive headings that capture content
- Transform questions posed to audience into declarative teaching statements where appropriate
- Use formatting (bold, italics, lists, blockquotes) to improve readability
- Add paragraph breaks for better flow
- Create smooth transitions between sections

### Content Organization Strategy

1. **Introduction Section**: Overview/big picture from first video(s)

2. **Main Chapters**: Group by theme, not necessarily by video

3. **Subsections**: Break chapters into digestible pieces (3.1, 3.2, etc.)

4. **Examples**: Keep inline but clearly formatted

5. **Summary**: Synthesize key takeaways across all content

### File Naming Pattern Recognition

Common patterns to look for:

- Sequential numbering: `3.7.1`, `3.7.2`, `3.7.3`
- Hierarchical structure: `3.7` = Chapter 7 of Module 3, `.1` = first subsection
- File modification timestamps as fallback ordering method
- Descriptive names in ALL CAPS (e.g., "DOMAIN SPECIFIC POLICY")

### Quality Checks

Before finalizing:

- All source files incorporated in correct order
- No transcript artifacts remain
- Examples are complete and make sense
- Headings create clear hierarchy
- Transitions between sections are smooth
- Technical terms are used consistently
- Summary captures all major themes
- Document is formatted with proper Markdown syntax
* * *

## Usage Example

**User says:** "This directory contains transcripts for videos that I am to watch for my introduction to Economics course, specifically Module 5 on Supply and Demand. Can you create a new Markdown document that formats the content into prose with mild edits so I can read it more like a textbook. The documents were downloaded in order they should be watched so earlier timestamps means that document should be earlier in your combined markdown document."

**AI should:**

1. Run `ls -lt` to see files and timestamps

2. Read all transcript files in parallel

3. Identify the content themes (e.g., supply curves, demand curves, equilibrium, elasticity)

4. Create logical chapter structure

5. Transform conversational text to textbook prose

6. Output as `Module_5_Reading.md`

* * *

## Notes for Future Iterations

### Lessons Learned from Module 3 Processing

1. **File Order Detection**: File modification times combined with filename patterns (3.7.1, 3.7.2, etc.) provide clear ordering

2. **Natural Content Groupings**: Videos often cluster around themes even if in different numerical sequences (e.g., all policy videos, all ethics videos)

3. **Title Extraction**: Video titles in filenames (in ALL CAPS) are useful for creating section headings

4. **Preserving Voice**: Keep phrases like "I hope you remember this one-liner" or "I encourage you to" - they add personality while still being professional

5. **Examples are Gold**: Real-world examples and scenarios are the most valuable content to preserve exactly

6. **Introduction Videos**: Usually the first video provides the best overview for an introduction section

7. **Cross-References**: When content mentions "we'll talk about this elsewhere," maintain those references

8. **Action Items**: Convert "you should do X" into clear recommendations or principles

### Common Transcript Artifacts to Remove

- "Let's go through..." → Start directly with the content
- Repeated "Now..." at the start of paragraphs
- "You know" and hedging language
- "So" at the beginning of sentences
- Line breaks mid-sentence from speech patterns
- Redundant re-statements from verbal emphasis

### Markdown Formatting Best Practices

- Use `#` for main title, `##` for chapters, `###` for sections, `####` for subsections
- Use `**bold**` for key terms on first use
- Use `>` blockquotes for important principles or quotes
- Use `-` or `1.` for lists
- Use `---` for horizontal rules between major sections
- Use `**italic**` sparingly for emphasis