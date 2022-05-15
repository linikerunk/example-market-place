import styled from "styled-components";

export const BackgroundModal = styled.div`
  background-color: rgba(0, 0, 0, 0.8);
  justify-content: center;
  align-items: center;
  height: 102vh;
  width: 100%;
  display: flex;
  position: absolute;
  bottom: 0;
  right: 0;
  left: 0;
  top: 0;
`;

export const Modal = styled.div`
  background-color: #ffff;
  justify-content: center;
  border-radius: 0.4rem;
  margin-top: 2rem;
  position: static;
  margin: 0 auto;
  display: flex;
  height: 33rem;
  width: 51rem;

  p {
    text-align: center;
    font-size: 2.5rem;
  }
`;

export const Form = styled.form`

`

export const containerModal = styled.div`
  margin: 2rem auto;
  position: static;
`;

export const ContainerInput = styled.div`
  position: static;
  margin-top: 3rem;
`;

export const ContainerButton = styled.div`
  justify-content: space-around;
  align-items: center;
  margin-top: 2rem;
  position: static;
  display: flex;
`;
