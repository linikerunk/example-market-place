import styled from 'styled-components'

export const Wrapper = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
`

export const Overlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.8);
  cursor: pointer;
`

export const Card = styled.div`
  position: relative;
  display: flex;
  padding: 2rem;
  flex-direction: column;
  align-items: center;
  height: auto;
  width: 51rem;
  background-color: #fff;
  border-radius: 0.4rem;
  z-index: 1;
  @media (max-width: 560px) {
    width: 90%;
    flex-direction: column;
  }
`

export const ButtonClose = styled.span`
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 0;
  right: 0;
  padding: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  &:hover {
    background-color: #ddd;
    border-radius: 50%;
  }
  @media (max-width: 560px) {
    img {
      padding: 0.3rem !important;
      background-color: #fff !important;
      border-radius: 0.4rem !important;
    }
  }
`

export const ContainerButton = styled.div`
  display: flex;
  margin-top: 10rem;

  button + button {
    margin-left: 10rem;
  }
`;

export const Content = styled.div`
  display: flex;
  flex-direction: column;
`

export const Title = styled.h1`
  font-weight: normal;
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 5rem;
`