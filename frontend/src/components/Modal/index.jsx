import { useEffect } from 'react'

import { Button } from '../Button'
import { Input } from '../Input'

import * as S from './styles'

export function Modal({ isExit, setIsExit }) {

  function handleSubmit(event) {
    event.preventDefault()
  }

  useEffect(() => {
    isExit
      ? (document.body.style.overflow = 'hidden')
      : (document.body.style.overflow = 'visible')
  }, [isExit])

  return (
    <S.BackgroundModal>
      <S.Modal>
        <S.containerModal>
          <p>Cadastro de Serviços</p>
          <S.Form onSubmit={handleSubmit} method={"post"}>
          <S.ContainerInput>
              <Input text={"Nome do Vendedor:"} type={"text"} widthInput={"40rem"}/>
            </S.ContainerInput>
            <S.ContainerInput>
              <Input text={"Nome do Produto:"} type={"text"} widthInput={"40rem"}/>
            </S.ContainerInput>
            <S.ContainerInput>
              <Input text="Preço:" type={"text"} widthInput={"40rem"}/>
            </S.ContainerInput>
            <S.ContainerInput>
              <Input text="Comissão:" type={"text"} widthInput={"40rem"}/>
            </S.ContainerInput>
            <S.ContainerButton>
              <Button type="submit" color={"#049237"}>Continuar</Button>
              <Button color={"#1137f1ed"} click={() => setIsExit(false)}>Cancelar</Button>
            </S.ContainerButton>
          </S.Form>
        </S.containerModal>
      </S.Modal>
    </S.BackgroundModal>
  )
}