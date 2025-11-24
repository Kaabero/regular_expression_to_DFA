  export const Notification = ({message}) => {
    if (message != '') {
      return (
        <div className="notification">
            <p> { message } </p>
        </div>
      )
    }
  }