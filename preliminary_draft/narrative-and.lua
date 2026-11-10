-- narrative-and.lua
-- APA 7 writes "and" between authors in narrative citations ("Kang and Chen
-- (2008) argue") and "&" only inside parentheses ("(Kang & Chen, 2008)").
-- citeproc cannot make that distinction with the APA CSL. Quarto cannot place
-- a filter after its citeproc step, so this filter runs citeproc itself
-- (the YAML sets `citeproc: false` to avoid a second run) and then replaces
-- the "&" in the author part of narrative (AuthorInText) citations.
-- Parenthetical citations and the reference list are not touched.

local function narrative_and(cite)
  if cite.citations[1].mode ~= "AuthorInText" then
    return nil
  end
  local in_parens = false
  cite.content = cite.content:walk({
    Str = function(s)
      -- only the author names before the "(" of the year are changed
      if s.text:find("%(") then in_parens = true end
      if not in_parens and s.text == "&" then
        return pandoc.Str("and")
      end
    end
  })
  return cite
end

function Pandoc(doc)
  doc = pandoc.utils.citeproc(doc)
  return doc:walk({ Cite = narrative_and })
end
