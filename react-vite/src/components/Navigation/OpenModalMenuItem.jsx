import { useModal } from "../../context/Modal";
import profile from "./ProfileButton.module.css";

function OpenModalMenuItem({
  modalComponent,
  itemText,
  onItemClick,
  onModalClose,
}) {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (typeof onItemClick === "function") onItemClick();
  };

  return (
    <div onClick={onClick}>
      <button className={profile.modalButton}>{itemText}</button>
    </div>
  );
}


export default OpenModalMenuItem;
