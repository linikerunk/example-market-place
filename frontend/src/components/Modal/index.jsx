import { useEffect, useState } from 'react'

import { Button } from '../Button'
import { Input } from '../Input'
import { API } from '../../services/api'

import * as S from './styles'

export function Modal({ isExit, setIsExit }) {
  const [sellerName, setSellerName] = useState('')
  const [nameProduct, setNameProduct] = useState('')
  const [price, setPrice] = useState('')
  const [comission, setComission] = useState('')
  const [isProduct, setIsProduct] = useState(false)

  const [sellers, setSellers] = useState([]);

  async function getData() {
    const response = await API.get("sellers/");
    setSellers(response.data);
  }

  useEffect(() => {
    getData();
  }, []);


  async function handleSubmit(event) {
    event.preventDefault()

    const response = await API.post()
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
              <label>Nome do Vendedor</label>
            <select name="" id="">
              {sellers.map(({ name }) => (
                <option>{name}</option>
              ))}
            </select>
            </S.ContainerInput>
            <S.ContainerInput>
              <Input text={"Nome do Produto:"} type="text" widthInput={"40rem"} name="product_name"/>
            </S.ContainerInput>
            <S.ContainerInput>
              <Input text="Preço:" type="text" widthInput={"40rem"} name="price"/>
            </S.ContainerInput>
            <S.ContainerInput>
              <Input text="Comissão:" type="text" widthInput={"40rem"} name="comission" />
            </S.ContainerInput>
            <S.ContainerInput>
            <Input text="Serviço:" type="checkbox" name="comission" />
            </S.ContainerInput>
            <S.ContainerButton>
              <Button type="submit" color={"#049237"} click={handleSubmit}>Continuar</Button>
              <Button color={"#1137f1ed"} click={() => setIsExit(false)}>Cancelar</Button>
            </S.ContainerButton>
          </S.Form>
        </S.containerModal>
      </S.Modal>
    </S.BackgroundModal>
  )
}