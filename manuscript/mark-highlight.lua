-- mark-highlight.lua
-- Makes spans written as [text]{.mark} visibly highlighted (yellow) in the
-- formats defined by the imrad-apa template (docx, pdf).
-- HTML needs no filter: pandoc renders such spans as <mark>, which browsers
-- highlight by default.

local function xml_escape(s)
  s = s:gsub("&", "&amp;")
  s = s:gsub("<", "&lt;")
  s = s:gsub(">", "&gt;")
  return s
end

local function docx_run(text, bold)
  local rpr = "<w:rPr>" .. (bold and "<w:b/>" or "") ..
    '<w:highlight w:val="yellow"/></w:rPr>'
  return pandoc.RawInline("openxml",
    "<w:r>" .. rpr .. '<w:t xml:space="preserve">' .. xml_escape(text) ..
    "</w:t></w:r>")
end

function Span(el)
  if not el.classes:includes("mark") then
    return nil
  end

  if quarto.doc.is_format("docx") then
    local out = {}
    local buffer = ""
    for _, inl in ipairs(el.content) do
      if inl.t == "Strong" then
        if buffer ~= "" then
          table.insert(out, docx_run(buffer, false))
          buffer = ""
        end
        table.insert(out, docx_run(pandoc.utils.stringify(inl), true))
      elseif inl.t == "Space" or inl.t == "SoftBreak" or inl.t == "LineBreak" then
        buffer = buffer .. " "
      else
        buffer = buffer .. pandoc.utils.stringify(inl)
      end
    end
    if buffer ~= "" then
      table.insert(out, docx_run(buffer, false))
    end
    return out
  elseif quarto.doc.is_format("latex") then
    local out = { pandoc.RawInline("latex", "\\hl{") }
    for _, inl in ipairs(el.content) do
      table.insert(out, inl)
    end
    table.insert(out, pandoc.RawInline("latex", "}"))
    return out
  end

  return nil
end
