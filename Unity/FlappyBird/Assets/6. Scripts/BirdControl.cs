using UnityEngine;
using UnityEngine.SceneManagement;

public class BirdControl : MonoBehaviour
{
    private Rigidbody _rigidbody;
    
    void Start()
    {
        Screen.SetResolution(480, 800, false);
        _rigidbody = GetComponent<Rigidbody>();
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            _rigidbody.velocity = new Vector3(0, 0, 0);
            _rigidbody.AddForce(0, 300, 0);
        }

        if (Input.GetKeyDown(KeyCode.R))
        {
            Time.timeScale = 1;
            SceneManager.LoadScene("Game");
        }
    }

    private void OnCollisionEnter(Collision collision)
    {
        Time.timeScale = 0;
        gameObject.GetComponent<Animator>().Play("Die");
    }
}
