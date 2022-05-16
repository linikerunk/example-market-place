import { useEffect, useState } from 'react'
import { API } from '../../services/api'

import * as S from "./style";

export function Input({ text, type, min, widthInput, setData, onChange }) {
  const [search, setSearch] = useState("")

  useEffect(() => {
    async function getSearch() {
      const response = await API.get(`product_activitys/?&search=${search}`)
      setData(response.data)
    }
    getSearch()
  }, [search])
  
  return (
    <S.Wrapper>
      <span>{text}</span>
      <S.Input widthInput={widthInput} onChange={(event) => setSearch(event.target.value)} type={type} min={min} />
    </S.Wrapper>
  );
}
